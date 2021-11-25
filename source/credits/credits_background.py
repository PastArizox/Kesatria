import pygame
import constants as c
import colors.ultracolors as color
from source.credits.credits_objects import Credits

class BG(pygame.sprite.Sprite):
    def __init__(self):
        super(BG, self).__init__()
        # init image and rect
        self.image = pygame.Surface(c.DISPLAY_SIZE)
        self.color = color.GREY64
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        # init objects sprite group
        self.objects = pygame.sprite.Group()
        # init objects
        self.credits = Credits()
        # add objects to the group
        self.objects.add(self.credits)
        # basic vel
        self.vel_x = 0
        self.vel_y = 0

    def update(self, event_list):
        # update all objects in the group
        self.objects.update(event_list)
        # basic vel
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y