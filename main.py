import pygame
import os
import constants as c
import colors.ultracolors as color
from event_handler import EventHandler
from menus import Menus
from userinit.player import player

# init fonts & shit
pygame.mixer.pre_init(22050, -16, 2, 1024)
pygame.init()
pygame.font.init()
pygame.mixer.quit()
pygame.mixer.init(22050, -16, 2, 1024)

# Center the Game Application
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Display setup
pygame.display.set_caption(f"Kesatria | Connected as {player.username} | {player.IGFirstName} {player.IGLastName}")
display = pygame.display.set_mode(c.DISPLAY_SIZE, 0, 32)
clock = pygame.time.Clock()

# Object setup
event_handler = EventHandler()
menu = Menus(display)

# Music setup

running = True
while running:
    # Reduce CPU usage ?
    # pygame.time.wait(5)
    
    # Tick Clock
    clock.tick(c.FPS)

    # Handle Events
    event_list = pygame.event.get()
    event_handler.handle_events(event_list)

    # Handle menus
    menu.handle_menus(event_list, display)

    # Update the display
    pygame.display.update()