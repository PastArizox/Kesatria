import pygame
import constants as c
import colors.ultracolors as color

class Message(pygame.sprite.Sprite):
    def __init__(self):
        super(Message, self).__init__()
        self.font_size = 50
        self.font = pygame.font.Font(None, self.font_size)
        self.color = color.WHITE
        self.text = ""
        self.image = self.font.render(self.text, True, self.color, None)
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 10
        self.vel_x = 0
        self.vel_y = 0

    def update(self, event_list):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

    def send(self):
        pass