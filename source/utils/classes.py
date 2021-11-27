import pygame
import constants as c

class Button(pygame.sprite.Sprite):
    def __init__(self, image:str, x:int, y:int):
        super(Button, self).__init__()
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.snd_click = pygame.mixer.Sound(c.click_sound)
        self.vel_x = 0
        self.vel_y = 0

    def update(self, event_list):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

class Label(pygame.sprite.Sprite):
    def __init__(self, value:str, size:int, font, color, x:int, y:int):
        super(Label, self).__init__()
        self.value = value
        self.font_size = size
        self.font = pygame.font.Font(font, self.font_size)
        self.color = color
        self.image = self.font.render(self.value, True, self.color, None)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_x = 0
        self.vel_y = 0

    def update(self, event_list):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y