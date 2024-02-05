import pygame


class Text:
    def __init__(self, text, font_size=24, color=(255, 255, 255), pos=(0, 0)):
        self.z = 100
        self.text = text
        self.font_size = font_size
        self.color = color
        self.transparency = 255

        self.velocity = pygame.math.Vector2([0, 0])

        self.font = pygame.font.Font("assets\\Pixel-type.ttf", self.font_size)
        self.image = self.font.render(self.text, True, self.color)
        self.rect = pygame.rect.FRect(self.image.get_rect())

        self.rect.topleft = pos

    def update(self, new_text=None):

        if new_text:
            self.text = new_text

        self.rect.left += self.velocity.x
        self.rect.top += self.velocity.y

        self.image = self.font.render(self.text, True, self.color)
        self.image.set_alpha(self.transparency)

    def render(self, screen):
        screen.blit(self.image, self.rect.topleft)
