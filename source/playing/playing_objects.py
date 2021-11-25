import pygame
import constants as c
import colors.ultracolors as color
from userinit.player import player
import random


class Username(pygame.sprite.Sprite):
    def __init__(self):
        super(Username, self).__init__()
        self.player = player
        self.value = f"{self.player.IGFirstName} {self.player.IGLastName}"
        self.font_size = 60
        self.font = pygame.font.Font(None, self.font_size)
        self.color = color.WHITE
        self.image = self.font.render(self.value, True, self.color, None)
        self.rect = self.image.get_rect()
        self.rect.x = c.DISPLAY_WIDTH // 2 - self.rect.width // 2
        self.rect.y = self.player.rect.y - 50
        self.vel_x = 0
        self.vel_y = 0
    
    def update(self, event_list):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

class ButtonShop(pygame.sprite.Sprite):
    def __init__(self):
        super(ButtonShop, self).__init__()
        self.image = pygame.image.load(c.playing_button_shop).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = c.DISPLAY_WIDTH - self.rect.width - 10
        self.rect.y = c.DISPLAY_HEIGHT - self.rect.height - 10
        self.snd_click = pygame.mixer.Sound("sound\\button_click_sound.ogg")
        self.vel_x = 0
        self.vel_y = 0

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

class ButtonQuest(pygame.sprite.Sprite):
    def __init__(self):
        super(ButtonQuest, self).__init__()
        self.button_shop = ButtonShop()
        self.image = pygame.image.load(c.playing_button_quest).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = c.DISPLAY_WIDTH - self.rect.width - 10
        self.rect.y = self.button_shop.rect.y - self.rect.height - 10
        self.snd_click = pygame.mixer.Sound("sound\\button_click_sound.ogg")
        self.vel_x = 0
        self.vel_y = 0

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

class ButtonInventory(pygame.sprite.Sprite):
    def __init__(self):
        super(ButtonInventory, self).__init__()
        self.image = pygame.image.load(c.playing_button_inventory).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = c.DISPLAY_HEIGHT - self.rect.height - 10
        self.snd_click = pygame.mixer.Sound("sound\\button_click_sound.ogg")
        self.vel_x = 0
        self.vel_y = 0

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

class ButtonSettings(pygame.sprite.Sprite):
    def __init__(self):
        super(ButtonSettings, self).__init__()
        self.button_inventory = ButtonInventory()
        self.image = pygame.image.load(c.playing_button_settings).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = self.button_inventory.rect.y - self.rect.height - 10
        self.snd_click = pygame.mixer.Sound("sound\\button_click_sound.ogg")
        self.vel_x = 0
        self.vel_y = 0

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

class StatsLabel(pygame.sprite.Sprite):
    def __init__(self, value:str, x:int = 0, y:int = 0, var:int = None):
        super(StatsLabel, self).__init__()
        self.player = player
        self.var = var
        self.value = value
        self.font_size = 25
        self.font = pygame.font.Font(None, self.font_size)
        self.color = color.WHITE
        self.image = self.font.render(self.value, True, self.color, None)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_x = 0
        self.vel_y = 0
    
    def update(self, event_list):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y