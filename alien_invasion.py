import pygame

from settings import Settings

from ship import Ship

from alien import Alien

import game_functions as gf

from pygame.sprite import Group

def run_game():
    # Initialize game and create screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_height, ai_settings.screen_width))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(ai_settings, screen)
    # Make group to store bullets in
    bullets = Group()
    # Make an alien
    alien = Alien(ai_settings, screen)

    # Start main loop for the game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, alien, bullets)

run_game()
