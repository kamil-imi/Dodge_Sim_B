import pygame
from scripts.images import get_image_by_relative_path
from scripts.text import Text
from scripts.player import Player
from scripts.animation import MAnimationSys, FAnimationsSys


class Game:
    def __init__(self):
        pygame.init()

        self.window = pygame.display.set_mode((1450, 900), pygame.FULLSCREEN)
        pygame.display.set_caption("Dodging Simulator B")
        pygame.display.set_icon(get_image_by_relative_path("player\\0.png"))
        self.window_rect = self.window.get_rect()

        self.main = Main(self)
        self.menu = Menu(self)

        self.clock = pygame.time.Clock()
        self.on = True

    def run(self):
        while self.on:
            pygame.mouse.set_visible(False)
            self.window.fill((0, 0, 0))

            self.main.update()
            self.menu.update()

            self.main.draw()
            self.menu.draw()

            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()


class Base:
    def __init__(self, game):
        self.game = game
        self.background = pygame.surface.Surface((0, 0))
        self.unlock = False
        self.animation_sys = None
        self.sprites: dict = {"IDKHowToLeft": Text("press esc to left the game")}

    def draw(self):
        if self.unlock:
            for key in sorted(self.sprites.keys(), key=lambda k: self.sprites[k].z):
                self.game.window.blit(self.sprites[key].image, self.sprites[key].rect)


class Main(Base):
    def __init__(self, game):
        super().__init__(game)
        self.type = ""
        self.attacks = {}
        self.sprites = {"player": Player(self, a_type=self.type)}
        self.animation_sys = FAnimationsSys(self)

    def update(self):
        if self.unlock:
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    self.game.on = False
                if ev.type == pygame.KEYUP:
                    if ev.key == pygame.K_ESCAPE:
                        self.game.on = False

            self.animation_sys.update()
            for key in self.sprites.keys():
                self.sprites[key].update()
            for key in self.attacks.keys():
                self.sprites[key].update()


class Menu(Base):
    def __init__(self, game):
        super().__init__(game)
        self.animation_sys = MAnimationSys(self)
        self.unlock = True
        self.inputs = {
            "up": False,
            "down": False,
            "left": False,
            "right": False,
            "z": False,
            "x": False,
            "c": False
        }

    def update(self):
        if self.unlock:
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    self.game.on = False
                if ev.type == pygame.KEYUP:
                    if ev.key == pygame.K_ESCAPE:
                        self.game.on = False
                if ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_UP:
                        self.inputs["up"] = True
                    if ev.key == pygame.K_DOWN:
                        self.inputs["down"] = True
                    if ev.key == pygame.K_LEFT:
                        self.inputs["left"] = True
                    if ev.key == pygame.K_RIGHT:
                        self.inputs["right"] = True
                    if ev.key == pygame.K_z:
                        self.inputs["z"] = True
                    if ev.key == pygame.K_x:
                        self.inputs["x"] = True
                    if ev.key == pygame.K_c:
                        self.inputs["c"] = True

            self.animation_sys.update()

            for key in self.sprites.keys():
                self.sprites[key].update()

            for key in self.inputs:
                self.inputs[key] = False


if __name__ == "__main__":
    Game().run()
