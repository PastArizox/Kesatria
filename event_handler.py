import pygame
import constants as c
import json
from userinit.player import player

class EventHandler:
    def __init__(self):
        self.player = player
        self.username = self.player.username

    def handle_events(self, event_list):
        for event in event_list:
            if event.type == pygame.QUIT:
                self.save()
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    
                    for menu in c.MENUS:
                        if c.MENUS[menu] and menu != "PAUSE":
                            c.OLD_MENU = menu

                    if c.MENUS["PLAYING"]:
                        c.MENUS["PLAYING"] = False
                        c.MENUS["PAUSE"] = True

                    elif c.MENUS["CREDITS"]:
                        c.MENUS["CREDITS"] = False
                        c.MENUS["MAIN"] = True

                    elif c.MENUS["PAUSE"]:
                        c.MENUS["PAUSE"] = False
                        c.MENUS[c.OLD_MENU] = True

                    elif c.MENUS["SHOP"]:
                        c.MENUS["SHOP"] = False
                        c.MENUS["PLAYING"] = True

                    elif c.MENUS["QUEST"]:
                        c.MENUS["QUEST"] = False
                        c.MENUS["PLAYING"] = True

                    elif c.MENUS["INVENTORY"]:
                        c.MENUS["INVENTORY"] = False
                        c.MENUS["PLAYING"] = True

                    elif c.MENUS["SETTINGS"]:
                        c.MENUS["SETTINGS"] = False
                        c.MENUS["PLAYING"] = True

        # for menu in c.MENUS:
        #     if c.MENUS[menu]:
        #         print(menu)

        # print(c.OLD_MENU)

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

        users[self.username]["weapons"]["Activ Thorn"] = self.player.active_thorn[1]
        users[self.username]["weapons"]["Non-Activ Thorn"] = self.player.non_active_THORN[1]
        users[self.username]["weapons"]["Wood Sword"] = self.player.wood_sword[1]
        users[self.username]["weapons"]["Renforced Axe"] = self.player.renforced_sword[1]
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