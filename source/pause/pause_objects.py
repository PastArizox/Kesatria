import pygame
import constants as c
import colors.ultracolors as color
import json
from source.utils.classes import Button
from userinit.player import player

class BContinue(Button):
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

class BSave(Button):
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
        username = player.username
        users[username]["stats"]["life"] = player.life
        users[username]["stats"]["resistance"] = player.resistance
        users[username]["stats"]["determination"] = player.determination
        users[username]["stats"]["magic"] = player.magic
        users[username]["stats"]["gold"] = player.gold
        users[username]["stats"]["damage"] = player.damage
        users[username]["stats"]["level"] = player.level
        users[username]["stats"]["exp"] = player.exp

        users[username]["weapons"]["Active Thorn"] = player.active_thorn[1]
        users[username]["weapons"]["Non-Active Thorn"] = player.non_active_THORN[1]
        users[username]["weapons"]["Wood Sword"] = player.wood_sword[1]
        users[username]["weapons"]["Renforced Sword"] = player.renforced_sword[1]
        users[username]["weapons"]["Shadow Sword"] = player.shadow_sword[1]
        users[username]["weapons"]["Takeda Sword"] = player.takeda_sword[1]
        users[username]["weapons"]["Shinsu Sword"] = player.shinsu_sword[1]

        users[username]["armor"]["Wood Armor"] = player.wood_armor[1]
        users[username]["armor"]["Renforced Armor"] = player.renforced_armor[1]
        users[username]["armor"]["Shadow Armor"] = player.shadow_armor[1]
        users[username]["armor"]["Takeda Armor"] = player.takeda_armor[1]
        users[username]["armor"]["Shinsu Armor"] = player.shinsu_armor[1]

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

class BQuit(Button):
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