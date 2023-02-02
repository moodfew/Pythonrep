import pygame


class Rocket:
    """Klas the menaxhoj rraketen"""

    def __init__(self, r_game):
        """Initialize the rocket and set it's starting position"""
        
        self.screen = r_game.screen
        self.settings = r_game.settings
        self.screen_rect = r_game.screen.get_rect()

        # Load the image and define it's starting position
        self.image = pygame.image.load('images/rocket_small.png')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

        # Store a decimal value for rocket's horisontal and vertical positions
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags
        self.moving_right, self.moving_left = False, False
        self.moving_up, self.moving_down = False, False

    def update(self):
        """Update rocket's position based on the flags"""

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.rocket_speed
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.settings.rocket_speed

        # Update the rect object from position attributes
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the rocket at its current location"""
        self.screen.blit(self.image, self.rect)
