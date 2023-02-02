from collections.abc import Set
import pygame
import sys
from settings import Settings
from bird import Bird

class BlueBirdGame:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
                (self.settings.width, self.settings.height)
                                              )
        pygame.display.set_caption('Blue Bird Game')
        self.bird = Bird(self)
    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event == pygame.QUIT:
                sys.exit()
    def _update_screen(self):
        """Update images and flip them to new screen"""

        self.screen.fill(self.settings.bg_color)
        self.bird.blitme()
        pygame.display.flip()

if __name__ == '__main__':
    bbg = BlueBirdGame()
    bbg.run_game()

        
