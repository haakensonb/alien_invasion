import pygame

from pygame.sprite import Sprite


class Alien(Sprite):
    """Class to represent a single alien in the fleet"""

    def __init__(self, ai_settings, screen):
        """Initialize the alien and it's starting position"""
        super().__init__()
        self.ai_settings = ai_settings
        self.screen = screen

        # Load the alien image and set it's rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each alien at the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw alien at it's current location"""
        self.screen.blit(self.image, self.rect)
