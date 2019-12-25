from asciimatics.effects import Cycle, Snow
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen

def art(screen):
    effects = [
        Cycle(
            screen,
            FigletText("Merry Christmas!", font='big'),
            int(screen.height / 2 - 8)),
        Cycle(
            screen,
            FigletText("2019", font='big'),
            int(screen.height / 2 + 3)),
        Snow(screen)
    ]
    screen.play([Scene(effects, 500)])

Screen.wrapper(art)