import pygame
import constants as c
import colors.ultracolors as color
from userinit.player import player
from source.inventory.inventory_objects import Menu, Item, UnequipButton, EquipButton, ItemImage, StatsLabel, InfoLabel
from source.shop.shop_background import BG as BGShop

class BG(pygame.sprite.Sprite):
    def __init__(self):
        super(BG, self).__init__()
        # init image and rect
        self.image = pygame.image.load(c.inventory_background_black).convert_alpha()
        self.rect = self.image.get_rect()
        # init objects
        self.shop_background = BGShop()
        self.item_objects = self.shop_background.item_objects
        self.player = player
        self.item_image = ItemImage()
        self.unequip_button = UnequipButton()
        self.equip_button = EquipButton()
        self.menu = Menu()

        # init labels
        self.infos_label = InfoLabel()
        
        self.name_stats_label = StatsLabel(f"", 370)
        self.resist_stats_label = StatsLabel(f"", 400)
        self.deter_stats_label = StatsLabel(f"", 430)
        self.magic_stats_label = StatsLabel(f"", 460)
        self.damage_stats_label = StatsLabel(f"", 490)
        # init groups for sprite objects
        self.objects = pygame.sprite.Group()
        self.objects2 = pygame.sprite.Group()
        self.buttons_object = pygame.sprite.Group()
        # add objects to groups
        self.objects.add(self.menu)
        self.objects.add(self.item_image)
        self.objects.add(self.infos_label)
        self.objects.add(self.name_stats_label)
        self.objects.add(self.resist_stats_label)
        self.objects.add(self.deter_stats_label)
        self.objects.add(self.magic_stats_label)
        self.objects.add(self.damage_stats_label)

        self.buttons_object.add(self.unequip_button)
        self.buttons_object.add(self.equip_button)
        # init pos and index
        self.starting_x = 130
        self.offset_x = 120
        self.current_y = 120
        self.new_x = 0
        self.index = 0
        # basic vel
        self.vel_x = 0
        self.vel_y = 0

    def update(self, event_list):
        # update all objects in groups
        self.objects.update(event_list)
        self.objects2.update(event_list, self.unequip_button, self.equip_button, self.item_image, self.name_stats_label, self.resist_stats_label, self.deter_stats_label, self.magic_stats_label, self.damage_stats_label)
        self.buttons_object.update(event_list, self.player)
        self.add_items()
        # basic vel
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

    def add_items(self):
        for item in self.item_objects:
            if item.item[1] != 0:
                if item.item[8] != True:
                    if self.index < 5:
                        self.new_x = (self.starting_x) + self.offset_x * self.index
                        item = Item(item.item, item.image_path, self.new_x, self.current_y)
                        item.item[8] = True
                        self.objects2.add(item)
                        self.index +=1
                        # print(f"added {item.item[0]}")
                    else:
                        self.new_x = 0
                        self.index = 0
                        self.current_y += 120
                        self.new_x = (self.starting_x) + self.offset_x * self.index
                        item = Item(item.item, item.image_path, self.new_x, self.current_y)
                        item.item[8] = True
                        self.objects2.add(item)
                        self.index +=1