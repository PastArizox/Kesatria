import pygame
import constants as c
import colors.ultracolors as color

class ButtonPlay(pygame.sprite.Sprite):
    def __init__(self):
        super(ButtonPlay, self).__init__()
        self.width = 300
        self.height = 70
        self.size = (self.width, self.height)
        self.image = pygame.image.load(c.main_menu_play_button).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = c.DISPLAY_WIDTH // 2 - self.width // 2
        self.rect.y = c.DISPLAY_HEIGHT // 2 - 10
        self.snd_click = pygame.mixer.Sound("sound\\button_click_sound.ogg")
        self.vel_x = 0
        self.vel_y = 0

    def update(self, event_list):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    
                    for menu in c.MENUS:
                        if c.MENUS[menu] and menu != "PAUSE":
                            c.OLD_MENU = menu

                    # Play button sound
                    self.snd_click.play()
                    # Change menu
                    c.MENUS["MAIN"] = False
                    c.MENUS["PLAYING"] = True



class ButtonCredits(pygame.sprite.Sprite):
    def __init__(self):
        super(ButtonCredits, self).__init__()
        self.width = 300
        self.height = 70
        self.size = (self.width, self.height)
        self.image = pygame.image.load(c.main_menu_credits_button).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = c.DISPLAY_WIDTH // 2 - self.width // 2
        self.rect.y = c.DISPLAY_HEIGHT // 2 + 100
        self.snd_click = pygame.mixer.Sound("sound\\button_click_sound.ogg")
        self.vel_x = 0
        self.vel_y = 0

    def update(self, event_list):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):

                    for menu in c.MENUS:
                        if c.MENUS[menu] and menu != "PAUSE":
                            c.OLD_MENU = menu

                    # Play button sound
                    self.snd_click.play()
                    # Change menu
                    c.MENUS["MAIN"] = False
                    c.MENUS["CREDITS"] = True

class Title(pygame.sprite.Sprite):
    def __init__(self):
        super(Title, self).__init__()
        self.width = 700
        self.height = 100
        self.size = (self.width, self.height)
        self.image = pygame.image.load(c.main_menu_title).convert_alpha()
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect()
        self.rect.x = c.DISPLAY_WIDTH // 2 - self.width // 2
        self.rect.y = 70
        self.vel_x = 0
        self.vel_y = 0

    def update(self, event_list):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y