import pygame

class Bird:
    """A class to manage the Bird"""
    def __init__(self, bbg_game):
        """Initialize the bird and set its starting position"""

        self.screen = bbg_game.screen
        self.screen_rect = bbg_game.screen.get_rect()

        # Load the bird image and get its rect
        self.image = pygame.image.load('images/bird_small.bmp')
        self.rect = self.image.get_rect()

        # Start each new bird at the center
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Load the bird at its current location"""
        self.screen.blit(self.image, self.rect)
        
