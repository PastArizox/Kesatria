from tkinter import Message
import pygame
import constants as c
import colors.ultracolors as color
from userinit.player import player
# from userinit.mess import message

class Menu(pygame.sprite.Sprite):
    def __init__(self):
        super(Menu, self).__init__()
        self.image = pygame.image.load(c.shop_background).convert_alpha()
        self.rect = self.image.get_rect()
        self.vel_x = 0
        self.vel_y = 0

    def update(self, event_list):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

class Item(pygame.sprite.Sprite):
    def __init__(self, item:dict, image:str, x:int, y:int):
        super(Item, self).__init__()
        self.player = player
        self.width = 100
        self.height = 100
        self.size = (self.width, self.height)
        self.item = item
        self.image_path = image
        self.not_sized_image = pygame.image.load(image).convert_alpha()
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.snd_click = pygame.mixer.Sound("sound\\button_click_sound.ogg")
        self.vel_x = 0
        self.vel_y = 0

    def update(self, event_list, item_image, name, resist, deter, magic, dmg, price, buy_button):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    # Play button sound
                    self.snd_click.play()
                    item_image.image = self.not_sized_image
                    item_image.image = pygame.transform.scale(item_image.image, item_image.size)

                    buy_button.image = pygame.image.load(c.shop_buy_button).convert_alpha()
                    buy_button.image = pygame.transform.scale(buy_button.image, (224, 55))
                    buy_button.item = self.item

                    name.value = f"Name : {self.item[0]}"
                    resist.value = f"Resistance: {self.item[5]}"
                    deter.value = f"Determination: {self.item[6]}"
                    magic.value = f"Magic: {self.item[7]}"
                    dmg.value = f"Damage: {self.item[3]}"
                    price.value = f"Price: {self.item[2]} Golds"

                    name.image = name.font.render(name.value, True, name.color, None)
                    resist.image = resist.font.render(resist.value, True, resist.color, None)
                    deter.image = deter.font.render(deter.value, True, deter.color, None)
                    magic.image = magic.font.render(magic.value, True, magic.color, None)
                    dmg.image = dmg.font.render(dmg.value, True, dmg.color, None)
                    price.image = price.font.render(price.value, True, price.color, None)
                    
                    # print(f"{self.item}")

class ItemImage(pygame.sprite.Sprite):
    def __init__(self):
        super(ItemImage, self).__init__()
        self.player = player
        self.width = 200
        self.height = 200
        self.size = (self.width, self.height)
        self.image = pygame.image.load(c.shop_default_icon_item_image).convert_alpha()
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect()
        self.rect.x = 814
        self.rect.y = 150
        self.vel_x = 0
        self.vel_y = 0

    def update(self, event_list):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

class BuyButton(pygame.sprite.Sprite):
    def __init__(self):
        super(BuyButton, self).__init__()
        self.item = []
        self.image = pygame.image.load(c.shop_default_icon_item_image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (224, 55))
        self.rect = self.image.get_rect()
        self.rect.x = 798
        self.rect.y = 570
        self.snd_click = pygame.mixer.Sound("sound\\button_click_sound.ogg")
        self.vel_x = 0
        self.vel_y = 0

    def update(self, event_list, player):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    if not self.item == []:
                        # Play button sound
                        self.snd_click.play()
                        # Buy Object
                        if self.item[1] == 0:
                            if not player.gold < self.item[2]:
                                self.buy(player, self.item)
                            else:
                                print("You don't have enough gold")
                        else:
                            # message.text = "Hello World"
                            print("You already have this item")
                    

    def buy(self, player, item):
        print(f"{player.username} bought {item[0]}")
        print(player.gold)
        item[1] = 1
        player.gold -= item[2]
        print(player.gold)