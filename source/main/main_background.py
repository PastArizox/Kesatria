import pygame
import constants as c
import colors.ultracolors as color
import random
from source.main.main_objects import ButtonPlay, ButtonCredits, Title

class BG(pygame.sprite.Sprite):
    def __init__(self):
        super(BG, self).__init__()
        # init image and rect
        self.image = pygame.Surface(c.DISPLAY_SIZE)
        self.color = (color.NEON_BLUE)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        # init objects
        self.button_play = ButtonPlay()
        self.button_credits = ButtonCredits()
        self.title = Title()
        # init sprite group for objects
        self.objects = pygame.sprite.Group()
        # add objects to the group
        self.objects.add(self.button_play)
        self.objects.add(self.button_credits)
        self.objects.add(self.title)
        # basic vel
        self.vel_x = 0
        self.vel_y = 0

    def update(self, event_list):
        # update all objects in group
        self.objects.update(event_list)
        # basic vel
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y