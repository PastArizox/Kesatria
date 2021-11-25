import pygame
import constants as c
import colors.ultracolors as color

class Credits(pygame.sprite.Sprite):
    def __init__(self):
        super(Credits, self).__init__()
        self.image = pygame.image.load(c.credits_image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = c.DISPLAY_WIDTH // 2 - self.rect.width // 2
        self.rect.y = c.DISPLAY_HEIGHT // 2 - self.rect.height // 2
        self.vel_x = 0
        self.vel_y = 0

    def update(self, event_list):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y