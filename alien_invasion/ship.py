import pygame

class Ship:
    """A class to manage ships"""

    def __init__(self, ai):
        """Initialize the ship and set it's starting position"""

        self.screen = ai.screen
        self.screen_rect = ai.screen.get_rect()
        self.settings = ai.settings

        # Load the ship and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horisontal position
        self.x = float(self.rect.x)

        # Movement Flag
        self.moving_right = False
        self.moving_left = False
    def update(self):
        """Update the ship's movement based on movement flag"""

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

        
