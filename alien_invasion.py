import sys

import pygame

from settings import Settings

def run_game():
    # Initialize game and create screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_height, ai_settings.screen_width))
    pygame.display.set_caption("Alien Invasion")

    # Set the background color
    bg_color = (230, 230, 230)

    # Start main loop for the game
    while True:

        # Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraw screen during each pass through the loop
        screen.fill(ai_settings.bg_color)

        # Make the most recently drawn screen visible
        pygame.display.flip()

run_game()
