import pygame
import constants as c
import colors.ultracolors as color
from userinit.player import player
from source.utils.classes import Label
# from source.playing.playing_objects import ButtonShop, ButtonQuest, Username, StatsLabel, ButtonInventory, ButtonSettings
from source.playing.playing_objects import BShop, BInventory, BQuest, BSettings

class BG(pygame.sprite.Sprite):
    def __init__(self):
        super(BG, self).__init__()
        # init image and rect
        self.image = pygame.image.load(c.playing_background).convert_alpha()
        self.image = pygame.transform.scale(self.image, (c.DISPLAY_SIZE))
        self.rect = self.image.get_rect()
        # init player and objects
        self.player = player
        self.player.image = self.player.image.convert_alpha()

        self.button_shop = BShop(c.playing_button_shop, 10, c.DISPLAY_HEIGHT - 80)
        self.button_quest = BQuest(c.playing_button_quest, self.button_shop.rect.x, self.button_shop.rect.y - 80)
        self.button_inventory = BInventory(c.playing_button_inventory, self.button_quest.rect.x, self.button_quest.rect.y - 80)
        self.button_settings = BSettings(c.playing_button_settings, self.button_inventory.rect.x, self.button_inventory.rect.y - 80)

        self.player_name = Label(f"{self.player.IGFirstName} {self.player.IGLastName}", 60, None, color.WHITE, 0, 0)
        self.player_name.rect.x = c.DISPLAY_WIDTH // 2 - self.player_name.rect.width // 2
        self.player_name.rect.y = self.player.rect.y - 50
        self.player_life = Label(f"Life: {self.player.life}", 25, None, color.WHITE, 10, 10)
        self.player_resist = Label(f"Resistance: {self.player.resistance}", 25, None, color.WHITE, 10, 30)
        self.player_damage = Label(f"Damage: {self.player.damage}", 25, None, color.WHITE, 10, 90)
        self.player_deter = Label(f"Determination: {self.player.determination}", 25, None, color.WHITE, 10, 50)
        self.player_exp = Label(f"Experience: {self.player.exp}/{self.player.exp_needed}", 25, None, color.WHITE, 10, 130)
        self.player_gold = Label(f"Gold: {self.player.gold}", 25, None, color.WHITE, 0, 10)
        self.player_gold.rect.x = c.DISPLAY_WIDTH - self.player_gold.rect.width - 10
        self.player_level = Label(f"Level: {self.player.level}", 25, None, color.WHITE, 10, 110)
        self.player_magic = Label(f"Magic: {self.player.magic}", 25, None, color.WHITE, 10, 70)
        # init sprite group for objects
        self.objects = pygame.sprite.Group()
        # add objects to the sprite group
        self.objects.add(self.player)
        self.objects.add(self.button_shop)
        self.objects.add(self.button_quest)
        self.objects.add(self.button_inventory)
        self.objects.add(self.button_settings)
        self.objects.add(self.player_name)
        self.objects.add(self.player_life)
        self.objects.add(self.player_resist)
        self.objects.add(self.player_damage)
        self.objects.add(self.player_deter)
        self.objects.add(self.player_exp)
        self.objects.add(self.player_gold)
        self.objects.add(self.player_level)
        self.objects.add(self.player_magic)

        # update text
        self.player_gold.value = f"Gold: {self.player.gold}"
        self.player_life.value = f"Life: {self.player.life}"
        self.player_resist.value = f"Resistance: {self.player.resistance}"
        self.player_damage.value = f"Damage: {self.player.damage}"
        self.player_deter.value = f"Determination: {self.player.determination}"
        self.player_exp.value = f"Experience: {self.player.exp}/{self.player.exp_needed}"
        self.player_level.value = f"Level: {self.player.level}"
        self.player_magic.value = f"Magic: {self.player.magic}"
        # render the font
        self.player_gold.image = self.player_gold.font.render(self.player_gold.value, True, self.player_gold.color, None)
        self.player_life.image = self.player_life.font.render(self.player_life.value, True, self.player_life.color, None)
        self.player_resist.image = self.player_resist.font.render(self.player_resist.value, True, self.player_resist.color, None)
        self.player_damage.image = self.player_damage.font.render(self.player_damage.value, True, self.player_damage.color, None)
        self.player_deter.image = self.player_deter.font.render(self.player_deter.value, True, self.player_deter.color, None)
        self.player_exp.image = self.player_exp.font.render(self.player_exp.value, True, self.player_exp.color, None)
        self.player_level.image = self.player_level.font.render(self.player_level.value, True, self.player_level.color, None)
        self.player_magic.image = self.player_magic.font.render(self.player_magic.value, True, self.player_magic.color, None)

        # vasic vel
        self.vel_x = 0
        self.vel_y = 0

    def update(self, event_list):
        # update all objects in the group
        self.objects.update(event_list)
        
        # basic vel
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y