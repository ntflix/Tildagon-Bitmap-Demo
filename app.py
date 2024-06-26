import app
from .rhubarbandcustard import RhubarbAndCustard
from .leds import LEDManager
from . import heartimage as heartimage
import asyncio

from events.input import Buttons, BUTTON_TYPES
from system.patterndisplay.events import *
from system.eventbus import eventbus
from tildagonos import tildagonos


class HeartApp(app.App):
    screen_size = ((-120, -120), (240, 240))
    led_manager: LEDManager = LEDManager()
    on_color = (220, 11, 141)
    color: tuple[int, int, int] = on_color
    on: bool = True
    image_path: str = "/apps/heart/heart.bmp"
    party_task = None

    def __init__(self):
        self.button_states = Buttons(self)
        eventbus.emit(PatternDisable())
        tildagonos.init_display()
        self.draw_heart()

    def stop_party(self):
        if self.party_task:
            self.party_task.cancel()
            self.party_task = None

    def update(self, delta):
        if self.button_states.get(BUTTON_TYPES["RIGHT"]):
            self.stop_party()
            self.toggle()
        if self.button_states.get(BUTTON_TYPES["LEFT"]):
            self.stop_party()
            self.draw_heart()
        if self.button_states.get(BUTTON_TYPES["DOWN"]):
            self.party()
        elif self.button_states.get(BUTTON_TYPES["CANCEL"]):
            self.stop_party()
            # The button_states do not update while you are in the background.
            # Calling clear() ensures the next time you open the app, it stays open.
            # Without it the app would close again immediately.
            self.button_states.clear()

    def draw(self, ctx):
        ctx.save()
        # ctx.font_size = 20
        # ctx.text_align = ctx.CENTER
        # ctx.text_baseline = ctx.MIDDLE
        ctx.rgb(
            self.color[0],
            self.color[1],
            self.color[2],
        ).rectangle(
            self.screen_size[0][0],
            self.screen_size[0][1],
            self.screen_size[1][0],
            self.screen_size[1][1],
        ).fill()

        ctx.restore()

    def toggle(self):
        self.color = self.on_color if self.color == (0, 0, 0) else (0, 0, 0)
        self.on = not self.on

        if self.color == self.on_color:
            self.led_manager.on()
        else:
            self.led_manager.off()

    def draw_heart(self):
        tildagonos.tft.bitmap(heartimage, 50, 50)

    def party(self):
        # flick between pink and yellow like rhubarb and custard
        patterner = self.led_manager.do_pattern(RhubarbAndCustard())
        self.party_task = asyncio.create_task(patterner)


__app_export__ = HeartApp
