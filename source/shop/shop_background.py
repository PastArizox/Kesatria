import pygame
import constants as c
import colors.ultracolors as color
from source.shop.shop_objects import Menu, InfoLabel, Item, ItemImage, StatsLabel, BuyButton
from userinit.player import player

class BG(pygame.sprite.Sprite):
    def __init__(self):
        super(BG, self).__init__()
        # init player
        self.player = player
        # init image and rect
        self.image = pygame.image.load(c.shop_background).convert_alpha()
        self.rect = self.image.get_rect()
        self.menu = Menu()
        # init pos
        self.starting_x = 130
        self.starting_y = 120
        # init objects things
        self.item_image = ItemImage()
        self.item_wood_sword = Item(self.player.wood_sword, c.player_wood_sword, self.starting_x, self.starting_y)
        self.offset_x = (self.item_wood_sword.rect.width + 20)
        self.offset_y = (self.item_wood_sword.rect.height + 20)
        # init sword objects
        self.item_renforced_sword = Item(self.player.renforced_sword, c.player_renforced_sword, self.starting_x + self.offset_x * 1, self.starting_y + self.offset_y * 0)
        self.item_shadow_sword = Item(self.player.shadow_sword, c.player_shadow_sword, self.starting_x + self.offset_x * 2, self.starting_y + self.offset_y * 0)
        self.item_takeda_sword = Item(self.player.takeda_sword, c.player_takeda_sword, self.starting_x + self.offset_x * 3, self.starting_y + self.offset_y * 0)
        self.item_shinsu_sword = Item(self.player.shinsu_sword, c.player_shinsu_sword, self.starting_x + self.offset_x * 4, self.starting_y + self.offset_y * 0)
        # init armor objects
        self.item_wood_armor = Item(self.player.wood_armor, c.player_wood_armor, self.starting_x + self.offset_x * 0, self.starting_y + self.offset_y * 1)
        self.item_renforced_armor = Item(self.player.renforced_armor, c.player_renforced_armor, self.starting_x + self.offset_x * 1, self.starting_y + self.offset_y * 1)
        self.item_shadow_armor = Item(self.player.shadow_armor, c.player_shadow_armor, self.starting_x + self.offset_x * 2, self.starting_y + self.offset_y * 1)
        self.item_takeda_armor = Item(self.player.takeda_armor, c.player_takeda_armor, self.starting_x + self.offset_x * 3, self.starting_y + self.offset_y * 1)
        self.item_shinsu_armor = Item(self.player.shinsu_armor, c.player_shinsu_armor, self.starting_x + self.offset_x * 4, self.starting_y + self.offset_y * 1)
        # init thorn objects
        self.item_non_activ_THORN = Item(self.player.non_active_THORN, c.player_non_active_thorn, self.starting_x + self.offset_x * 0, self.starting_y + self.offset_y * 2)
        self.item_activ_thorn = Item(self.player.active_thorn, c.player_active_thorn, self.starting_x + self.offset_x * 1, self.starting_y + self.offset_y * 2)
        # init labels
        self.infos_label = InfoLabel()
        
        self.name_stats_label = StatsLabel(f"", 370)
        self.resist_stats_label = StatsLabel(f"", 400)
        self.deter_stats_label = StatsLabel(f"", 430)
        self.magic_stats_label = StatsLabel(f"", 460)
        self.damage_stats_label = StatsLabel(f"", 490)
        self.price_label = StatsLabel(f"", 520)
        # init buy button
        self.buy_button = BuyButton()
        # init objects sprite group (objects, item_objects, buttons)
        self.objects = pygame.sprite.Group()
        self.item_objects = pygame.sprite.Group()
        self.buttons = pygame.sprite.Group()
        # add objects to the groups
        self.objects.add(self.menu)
        self.objects.add(self.infos_label)
        self.objects.add(self.name_stats_label)
        self.objects.add(self.resist_stats_label)
        self.objects.add(self.deter_stats_label)
        self.objects.add(self.magic_stats_label)
        self.objects.add(self.damage_stats_label)
        self.objects.add(self.price_label)

        self.objects.add(self.item_image)
        
        self.item_objects.add(self.item_wood_sword)
        self.item_objects.add(self.item_renforced_sword)
        self.item_objects.add(self.item_shadow_sword)
        self.item_objects.add(self.item_takeda_sword)
        self.item_objects.add(self.item_shinsu_sword)

        self.item_objects.add(self.item_wood_armor)
        self.item_objects.add(self.item_renforced_armor)
        self.item_objects.add(self.item_shadow_armor)
        self.item_objects.add(self.item_takeda_armor)
        self.item_objects.add(self.item_shinsu_armor)

        self.item_objects.add(self.item_non_activ_THORN)
        self.item_objects.add(self.item_activ_thorn)

        self.buttons.add(self.buy_button)
        # basic vel
        self.vel_x = 0
        self.vel_y = 0

    def update(self, event_list):
        # update all objects in the groups
        self.objects.update(event_list)
        self.item_objects.update(event_list, self.item_image, self.name_stats_label, self.resist_stats_label, self.deter_stats_label, self.magic_stats_label, self.damage_stats_label, self.price_label, self.buy_button)
        self.buttons.update(event_list, self.player)
        # basic vel
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y