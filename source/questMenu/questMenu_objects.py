from tkinter import StringVar
import pygame
import constants as c
import colors.ultracolors as color
from userinit.player import player

class Menu(pygame.sprite.Sprite):
    def __init__(self):
        super(Menu, self).__init__()
        self.image = pygame.image.load(c.questMenu_background_black).convert_alpha()
        self.rect = self.image.get_rect()
        self.vel_x = 0
        self.vel_y = 0

    def update(self, event_list):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

class Button(pygame.sprite.Sprite):
    def __init__(self, image:StringVar):
        super(Button, self).__init__()
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.vel_x = 0
        self.vel_y = 0

    def update(self, event_list):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y