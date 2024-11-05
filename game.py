import pygame

from settings import Settings

class Game:
    '''Class to manage the game'''
    def __init__(self):
        '''Initialize the game and settings'''
        # Instance settings and clock
        self.settings = Settings()
        self.clock = pygame.time.Clock()
        # Instance and setup screen
        self.screen = pygame.display.set_mode(self.settings.screen_size)
        pygame.display.set_caption(self.settings.screen_caption)
        # Game loop flag attribute
        self.running = True

    def run(self):
        '''Runs the game main loop'''
        while self.running:
            self._update_events()
            self._update_screen()
    
    def _update_events(self):
        '''Updates the game events'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self._update_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._update_keyup_event(event)
    
    def _update_keydown_event(self, event):
        '''Updates a keydown event'''
        if event.key == pygame.K_ESCAPE:
            self.running = False
    
    def _update_keyup_event(self, event):
        '''Updates a keyup event'''
        pass
    
    def _update_screen(self):
        '''Updates the game screen'''
        self.screen.fill(self.settings.screen_color)

        pygame.display.flip()

        self.clock.tick(self.settings.screen_fps)

if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.run()
    pygame.quit()