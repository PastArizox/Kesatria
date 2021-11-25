import pygame
import constants as c
import colors.ultracolors as color
from source.main.main_background import BG as BGMain
from source.playing.playing_background import BG as BGPlaying
from source.pause.pause_background import BG as BGPause
from source.credits.credits_background import BG as BGCredits
from source.shop.shop_background import BG as BGShop
from source.inventory.inventory_background import BG as BGInventory
from source.questMenu.questMenu_background import BG as BGQuestMenu

# from userinit.mess import message

class Menus:
    def __init__(self, display):
        # Object setup
        self.main_bg = BGMain()
        self.main_bg_group = pygame.sprite.Group()
        self.main_bg_group.add(self.main_bg)

        self.playing_bg = BGPlaying()
        self.playing_bg_group = pygame.sprite.Group()
        self.playing_bg_group.add(self.playing_bg)

        self.pause_bg = BGPause()
        self.pause_bg_group = pygame.sprite.Group()
        self.pause_bg_group.add(self.pause_bg)

        self.credits_bg = BGCredits()
        self.credits_bg_group = pygame.sprite.Group()
        self.credits_bg_group.add(self.credits_bg)

        self.shop_bg = BGShop()
        self.shop_bg_group = pygame.sprite.Group()
        self.shop_bg_group.add(self.shop_bg)

        self.inventory_bg = BGInventory()
        self.inventory_bg_group = pygame.sprite.Group()
        self.inventory_bg_group.add(self.inventory_bg)

        self.questMenu_bg = BGQuestMenu()
        self.questMenu_bg_group = pygame.sprite.Group()
        self.questMenu_bg_group.add(self.questMenu_bg)

        # self.message_group = pygame.sprite.Group()
        # self.message_group.add(message)

    def handle_menus(self, event_list, display):
        if c.MENUS["MAIN"]:
            # Update all the objects
            self.main_bg_group.update(event_list)

            # Render the display
            self.main_bg_group.draw(display)
            self.main_bg.objects.draw(display)

        elif c.MENUS["CREDITS"]:
            # Update all the objects
            self.credits_bg_group.update(event_list)

            # Render the display
            self.credits_bg_group.draw(display)
            self.credits_bg.objects.draw(display)

        elif c.MENUS["PLAYING"]:
            # Update all the objects
            self.playing_bg_group.update(event_list)

            # Render the display
            self.playing_bg_group.draw(display)
            self.playing_bg.objects.draw(display)

        elif c.MENUS["PAUSE"]:

            # Update all the objects
            self.pause_bg_group.update(event_list)

            # Render the display
            self.pause_bg_group.draw(display)
            self.pause_bg.objects.draw(display)

        elif c.MENUS["SHOP"]:

            # Update all the objects
            self.shop_bg_group.update(event_list)

            # Render the display
            self.shop_bg_group.draw(display)
            self.shop_bg.objects.draw(display)
            self.shop_bg.item_objects.draw(display)
            self.shop_bg.buttons.draw(display)

        elif c.MENUS["QUEST"]:

            # Update all the objects
            self.questMenu_bg_group.update(event_list)

            # Render the display
            # display.fill(color.PALE_GREEN_1)
            self.questMenu_bg_group.draw(display)
            self.questMenu_bg.objects.draw(display)

        elif c.MENUS["INVENTORY"]:

            # Update all the objects
            self.inventory_bg_group.update(event_list)

            # Render the display
            self.inventory_bg_group.draw(display)
            self.inventory_bg.objects.draw(display)
            self.inventory_bg.objects2.draw(display)
            self.inventory_bg.buttons_object.draw(display)

        elif c.MENUS["SETTINGS"]:

            # Update all the objects
            pass

            # Render the display
            display.fill(color.GOLD_3)

        # self.message_group.draw(display)