import pygame
import constants as c
import colors.ultracolors as color
import random

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load(c.player_image)
        self.image = pygame.transform.scale(self.image, (c.PLAYER_SIZE))
        self.rect = self.image.get_rect()
        self.rect.x = c.DISPLAY_WIDTH // 2 - c.PLAYER_WIDTH // 2
        self.rect.y = c.DISPLAY_HEIGHT - c.PLAYER_HEIGHT - 70
        self.vel_x = 0
        self.vel_y = 0

        self.username = "Name"
        self.IGFirstName = "FirstName"
        self.IGLastName = "LastName"
        self.sex = "Male"

        self.life = 1000
        self.resistance = 50
        self.determination = 50
        self.magic = 50
        self.gold = 0
        self.damage = 50
        self.level = 1
        self.exp = 0

        self.max_health = 1000
        self.exp_needed = c.EXP[(self.level)-1]

        # TEMPLATE | self.object = [name, get_it[0, 1, 2], price, dmg, health, resist, deter, magic, IsInInventory]
        # THORNS
        self.active_thorn = ["Active Thorn", 0, 1000000, 25000000, 0, 0, 0, 0, False]
        self.non_active_THORN = ["Non-Active Thorn", 0, 500000, 10000000, 0, 0, 0, 0, False]
        # SWORDS
        self.wood_sword = ["Wood Sword", 0, 10, 0, 0, 0, 0, 0, False]
        self.renforced_sword = ["Renforced Sword", 0, 0, 0, 0, 0, 0, 0, False]
        self.shadow_sword = ["Shadow Sword", 0, 0, 0, 0, 0, 0, 0, False]
        self.takeda_sword = ["Takeda Sword", 0, 0, 0, 0, 0, 0, 0, False]
        self.shinsu_sword = ["Shinsu Sword", 0, 0, 0, 0, 0, 0, 0, False]
        # ARMORS
        self.wood_armor = ["Wood Armor", 0, 20, 0, 40, 20, 0, 0, False]
        self.renforced_armor = ["Renforced Armor", 0, 200, 20, 120, 60, 10, 0, False]
        self.shadow_armor = ["Shadow Armor", 0, 400, 0, 140, 20, 10, 80, False]
        self.takeda_armor = ["Takeda Armor", 0, 500, 40, 200, 100, 200, 0, False]
        self.shinsu_armor = ["Shinsu Armor", 0, 800, 60, 100, 120, 100, 60, False]

    def update(self, event_list):
        # KORO SENSEI SIMULATOR --> self.rect.x = random.randrange(0, c.DISPLAY_WIDTH - self.rect.width)
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y