import pygame
from scripts.time import Timer
from scripts.text import Text


type animation = Animation | dict[str: Animation]


class FAnimationsSys:
    ...


class MAnimationSys:
    def __init__(self, menu):
        self.menu = menu
        self.animation: Animation = MStart(self)
        self.step: int = 1

    def update(self):
        self.animation.update()

        if self.animation.end:
            self.step += 1

            match self.step:
                case 2:
                    self.animation = M(self)
                case 3:
                    self.animation = MEnd(self)


class Animation:
    ...


class MEnd(Animation):
    ...


class M(Animation):
    ...


class MStart(Animation):
    def __init__(self, animation_sys: MAnimationSys):
        self.animation_sys = animation_sys

        self.time_of_live = Timer(120)
        self.end = False

        self.animation_sys.menu.sprites["authorText"] = Text("By Kamilimi", 84, (255, 255, 255), (700, 900))
        self.animation_sys.menu.sprites["playButton"] = Text("Play", 84, (255, 255, 255), (100, 900))
        self.animation_sys.menu.sprites["settingsButton"] = Text("Settings", 84, (255, 255, 255), (100, 920))
        self.animation_sys.menu.sprites["extraButton"] = Text("Extra", 84, (255, 255, 255), (100, 940))

        self.sprites_help = [
            self.animation_sys.menu.sprites["authorText"],
            self.animation_sys.menu.sprites["playButton"],
            self.animation_sys.menu.sprites["settingsButton"],
            self.animation_sys.menu.sprites["extraButton"],
        ]

    def update(self):
        if self.time_of_live.current_tick >= 60:
            if self.time_of_live.current_tick == 60:
                self.sprites_help[0].velocity.y = -30
            else:
                self.sprites_help[0].velocity.y += 1

        self.time_of_live.update()

    def __bool__(self):
        return self.time_of_live.active
