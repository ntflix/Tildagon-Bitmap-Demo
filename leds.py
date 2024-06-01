from tildagonos import tildagonos


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
