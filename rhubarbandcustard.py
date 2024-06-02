from typing import Generator
from patterns.base import BasePattern

PINK = (255, 0, 255)
YELLOW = (255, 255, 0)


class RhubarbAndCustard(BasePattern):
    fps: float = 6.0
    _current_frame: int = 0
    frames: list[list[tuple[int, int, int]]] = [
        [PINK, PINK, YELLOW, YELLOW] * 6,
        [YELLOW, PINK, PINK, YELLOW] * 6,
        [YELLOW, YELLOW, PINK, PINK] * 6,
        [PINK, YELLOW, YELLOW, PINK] * 6,
    ]

    def __init__(self):
        # super().__init__()
        print(self.frames)

    @property
    def frame(self) -> list[tuple[int, int, int]]:
        return self.frames[self._current_frame]

    def next(self) -> list[tuple[int, int, int]]:
        # _current_frame = self._current_frame + 1
        self._current_frame = (self._current_frame + 1) % len(
            self.frames
        )  # wrap around
        return self.frame

    def current(self):
        return self.frame

    def pattern(self) -> Generator[list[tuple[int, int, int]], None, None]:
        while True:
            yield self.next()
