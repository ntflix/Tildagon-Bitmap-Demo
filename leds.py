# import time
# from .rhubarbandcustard import RhubarbAndCustard
from tildagonos import tildagonos
from patterns.base import BasePattern

import asyncio


class LEDManager:
    __color: tuple[int, int, int] = (220, 11, 141)

    def do_color(self):
        # asyncio.sleep(0.5)
        for i in range(1, 13):
            tildagonos.leds[i] = self.color
        tildagonos.leds.write()

    def __init__(self):
        self.do_color()

    def on(self):
        self.__color = (220, 11, 141)
        self.do_color()

    def off(self):
        self.__color = (0, 0, 0)
        self.do_color()

    def toggle(self):
        if self.__color == (220, 11, 141):
            self.off()
        else:
            self.on()

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value: tuple[int, int, int]):
        for i in value:
            if i < 0 or i > 255:
                raise ValueError("Color values must be between 0 and 255")

        self.__color = value
        self.do_color()

    async def do_pattern(self, pattern: BasePattern):
        """
        Example:
        class RhubarbAndCustard(BasePattern):
            fps: int = 6

            def __init__(self):
                super().__init__()
                self.fps = 11
                self.frame = [[PINK * 2, YELLOW * 2] * 6]

            def next(self):
                # shift all the pixels to the right, wrapping around
                self.frames[0][0] = self.frames[0][0][-1:] + self.frames[0][0][:-1]
                return self.frame

            def current(self):
                return self.frame
        """

        delay: float = 1.0 / pattern.fps
        try:
            while True:
                pattern_item = pattern.next()
                print(pattern_item)
                for i in range(1, 13):
                    tildagonos.leds[i] = pattern_item[i - 1]
                tildagonos.leds.write()
                await asyncio.sleep(delay)
                # time.sleep(delay)
        except asyncio.CancelledError:
            return
        finally:
            for i in range(1, 13):
                tildagonos.leds[i] = self.color
            tildagonos.leds.write()
            print("Pattern cancelled")
            # time.sleep(1)
