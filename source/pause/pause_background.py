import pygame
import constants as c
import colors.ultracolors as color
import random
from source.pause.pause_objects import BContinue, BQuit, BSave

class BG(pygame.sprite.Sprite):
    def __init__(self):
        super(BG, self).__init__()
        # init image and rect
        self.image = pygame.image.load(c.pause_menu_background).convert_alpha()
        self.rect = self.image.get_rect()
        # init objects
        self.button_continue = BContinue(c.pause_button_continue, 0, 0)
        self.button_continue.rect.x = c.DISPLAY_WIDTH // 2 - self.button_continue.rect.width // 2
        self.button_continue.rect.y = c.DISPLAY_HEIGHT // 2 - self.button_continue.rect.height // 2 - 100
        self.button_save = BSave(c.pause_button_save, self.button_continue.rect.x, self.button_continue.rect.y + 100)
        self.button_quit = BQuit(c.pause_button_quit, self.button_continue.rect.x, self.button_continue.rect.y + 200)
        # init sprite group for objects
        self.objects = pygame.sprite.Group()
        # add objects to group
        self.objects.add(self.button_continue)
        self.objects.add(self.button_save)
        self.objects.add(self.button_quit)
        # basic vel
        self.vel_x = 0
        self.vel_y = 0

    def update(self, event_list):
        # update all objects in group
        self.objects.update(event_list)
        # basic vel
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y