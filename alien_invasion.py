import pygame

from settings import Settings

from ship import Ship

import game_functions as gf

def run_game():
    # Initialize game and create screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_height, ai_settings.screen_width))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(screen)

    # Start main loop for the game
    while True:
        gf.check_events()

        gf.update_screen(ai_settings, screen, ship)

run_game()
