from player import Player
# init display consts
DISPLAY_WIDTH = 1150
DISPLAY_HEIGHT = 700
DISPLAY_SIZE = (DISPLAY_WIDTH, DISPLAY_HEIGHT)
# init player consts
PLAYER_WIDTH = 250
PLAYER_HEIGHT = 450
PLAYER_SIZE = (PLAYER_WIDTH, PLAYER_HEIGHT)
# init fps const
FPS = 30
# init actual used menu (true = in false = not in)
MENUS = {
    "MAIN" : True,
    "PLAYING": False,
    "PAUSE": False,
    "CREDITS": False,
    "SHOP": False,
    "QUEST": False,
    "INVENTORY": False,
    "SETTINGS": False,
    "LEVEL": False
}
# check for last menu used (for pause menu since we can pause int diff menus)
OLD_MENU = "NOTHING"
# basic exp values
EXP = [100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600, 51200,
102400, 204800, 409600, 819200, 1638400, 3276800,
6553600, 13107200, 26214400, 52428800, 104857600,
209715200, 419430400, 838860800, 1677721600, 3355443200,
6710886400, 13421772800, 26843545600, 53687091200, 107374182400,
214748364800, 429496729600, 858993459200, 1717986918400, 3435973836800,
6871947673600, 13743895347200, 27487790694400, 54975581388800, 109951162777600,
219902325555200, 439804651110400, 879609302220800, 1759218604441600,
3518437208883200, 7036874417766400, 14073748835532800, 28147497671065600]

# IMAGES

# credits menu
credits_image = "images\\credits\\credits_image.png"

# inventory menu
inventory_background_black = "images\\inventory\\inventory_background_black.png"
inventory_background = "images\\inventory\\inventory_background.png"
inventory_button_equip = "images\\inventory\\inventory_button_equip.png"
inventory_button_unequip = "images\\inventory\\inventory_button_unequip.png"

# main menu
main_menu_credits_button = "images\\main\\main_menu_credits_button.png"
main_menu_play_button = "images\\main\\main_menu_play_button.png"
main_menu_title = "images\\main\\main_menu_title.png"

# pause menu
pause_button_continue = "images\\pause\\pause_button_continue.png"
pause_button_quit = "images\\pause\\pause_button_quit.png"
pause_button_save = "images\\pause\\pause_button_save.png"
pause_menu_background = "images\\pause\\pause_menu_background.png"

# player image
player_image = "images\\player\\player_image.png"

# player items
player_renforced_armor = "images\\player\\player_renforced_armor.png"
player_renforced_sword = "images\\player\\player_renforced_sword.png"
player_shadow_armor = "images\\player\\player_shadow_armor.png"
player_shadow_sword = "images\\player\\player_shadow_sword.png"
player_shinsu_armor = "images\\player\\player_shinsu_armor.png"
player_shinsu_sword = "images\\player\\player_shinsu_sword.png"
player_takeda_armor = "images\\player\\player_takeda_armor.png"
player_takeda_sword = "images\\player\\player_takeda_sword.png"
player_wood_armor = "images\\player\\player_wood_armor.png"
player_wood_sword = "images\\player\\player_wood_sword.png"
# player thorns
player_active_thorn = "images\\player\\player_active_thorn.png"
player_non_active_thorn = "images\\player\\player_non_active_thorn.png"

# playing menu
playing_background = "images\\playing\\playing_background.png"
playing_button_inventory = "images\\playing\\playing_button_inventory.png"
playing_button_quest = "images\\playing\\playing_button_quest.png"
playing_button_settings = "images\\playing\\playing_button_settings.png"
playing_button_shop = "images\\playing\\playing_button_shop.png"

# shop menu
shop_background_black = "images\\shop\\shop_background_black.png"
shop_background = "images\\shop\\shop_background.png"
shop_buy_button = "images\\shop\\shop_buy_button.png"
shop_default_icon_item_image = "images\\shop\\shop_default_icon_item_image.png"
shop_default_icon = "images\\shop\\shop_default_icon.png"

# questMenu menu
questMenu_background_black = "images\\questMenu\\questMenu_background_black.png"

# SOUND
click_sound = "sound\\button_click_sound.ogg"