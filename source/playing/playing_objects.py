import pygame
import constants as c
from source.utils.classes import Button
from userinit.player import player

class BShop(Button):
    def update(self, event_list):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    # Play button sound
                    self.snd_click.play()
                    # Change menu
                    c.MENUS["PLAYING"] = False
                    c.MENUS["SHOP"] = True

class BQuest(Button):
    def update(self, event_list):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    # Play button sound
                    self.snd_click.play()
                    # Change menu
                    c.MENUS["PLAYING"] = False
                    c.MENUS["QUEST"] = True

class BInventory(Button):
    def update(self, event_list):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    # Play button sound
                    self.snd_click.play()
                    # Change menu
                    c.MENUS["PLAYING"] = False
                    c.MENUS["INVENTORY"] = True

class BSettings(Button):
    def update(self, event_list):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    # Play button sound
                    self.snd_click.play()
                    # Change menu
                    c.MENUS["PLAYING"] = False
                    c.MENUS["SETTINGS"] = True