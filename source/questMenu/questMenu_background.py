import pygame
import constants as c
import colors.ultracolors as colors
from userinit.player import player

class BG(pygame.sprite.Sprite):
    def __init__(self):
        super(BG, self).__init__()
        # init image and rect
        self.image = pygame.image.load(c.questMenu_background_black).convert_alpha()
        self.rect = self.image.get_rect()
        # init object sprite group
        self.objects = pygame.sprite.Group()
        # basic vel
        self.vel_x = 0
        self.vel_y = 0

    def update(self, event_list):
        pass