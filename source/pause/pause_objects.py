import pygame
import constants as c
import colors.ultracolors as color
import json
from userinit.player import player

class ButtonContinue(pygame.sprite.Sprite):
    def __init__(self):
        super(ButtonContinue, self).__init__()
        self.image = pygame.image.load(c.pause_button_continue).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = c.DISPLAY_WIDTH // 2 - self.rect.width // 2
        self.rect.y = c.DISPLAY_HEIGHT // 2 - self.rect.height // 2 - 100
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
                    c.MENUS["PAUSE"] = False
                    c.MENUS[c.OLD_MENU] = True

class ButtonSave(pygame.sprite.Sprite):
    def __init__(self):
        super(ButtonSave, self).__init__()
        self.player = player
        self.username = self.player.username
        self.image = pygame.image.load(c.pause_button_save).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = c.DISPLAY_WIDTH // 2 - self.rect.width // 2
        self.rect.y = c.DISPLAY_HEIGHT // 2 - self.rect.height // 2
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
                    # Save
                    self.save()

    def save(self):
        self.get_accounts_data()
        users = self.get_accounts_data()

        users[self.username]["stats"]["life"] = self.player.life
        users[self.username]["stats"]["resistance"] = self.player.resistance
        users[self.username]["stats"]["determination"] = self.player.determination
        users[self.username]["stats"]["magic"] = self.player.magic
        users[self.username]["stats"]["gold"] = self.player.gold
        users[self.username]["stats"]["damage"] = self.player.damage
        users[self.username]["stats"]["level"] = self.player.level
        users[self.username]["stats"]["exp"] = self.player.exp

        users[self.username]["weapons"]["Active Thorn"] = self.player.active_thorn[1]
        users[self.username]["weapons"]["Non-Active Thorn"] = self.player.non_active_THORN[1]
        users[self.username]["weapons"]["Wood Sword"] = self.player.wood_sword[1]
        users[self.username]["weapons"]["Renforced Sword"] = self.player.renforced_sword[1]
        users[self.username]["weapons"]["Shadow Sword"] = self.player.shadow_sword[1]
        users[self.username]["weapons"]["Takeda Sword"] = self.player.takeda_sword[1]
        users[self.username]["weapons"]["Shinsu Sword"] = self.player.shinsu_sword[1]

        users[self.username]["armor"]["Wood Armor"] = self.player.wood_armor[1]
        users[self.username]["armor"]["Renforced Armor"] = self.player.renforced_armor[1]
        users[self.username]["armor"]["Shadow Armor"] = self.player.shadow_armor[1]
        users[self.username]["armor"]["Takeda Armor"] = self.player.takeda_armor[1]
        users[self.username]["armor"]["Shinsu Armor"] = self.player.shinsu_armor[1]

        with open("./accounts.json", "w") as account:
            json.dump(users, account, indent = 4)

    def get_accounts_data(self):
        try:
            with open("./accounts.json", "r") as account:
                users = json.load(account)
        except IOError:
            with open("./accounts.json", "w") as f:
                f.write("{}")
            with open("./accounts.json", "r") as account:
                users = json.load(account)
        return users

class ButtonQuit(pygame.sprite.Sprite):
    def __init__(self):
        super(ButtonQuit, self).__init__()
        self.image = pygame.image.load(c.pause_button_quit).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = c.DISPLAY_WIDTH // 2 - self.rect.width // 2
        self.rect.y = c.DISPLAY_HEIGHT // 2 - self.rect.height // 2 + 100
        self.snd_click = pygame.mixer.Sound("sound\\button_click_sound.ogg")
        self.vel_x = 0
        self.vel_y = 0

    def update(self, event_list):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    # Save
                    
                    # Play button sound
                    self.snd_click.play()
                    # Change menu
                    c.MENUS["PAUSE"] = False
                    c.MENUS["MAIN"] = True