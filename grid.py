import pygame

class Grid:
    def __init__(self, game):
        self.screen = game.screen
        self.settings = game.settings
        self.rows = self.settings.grid_rows
        self.columns = self.settings.grid_columns
        self.color = self.settings.grid_color
    
    def blit(self):
        self._blit_rows()
        self._blit_columns()
    
    def _blit_rows(self):
        actual_row = 0
        while actual_row < self.rows:
            y = int(self.settings.screen_height / self.rows * actual_row)
            
            start_pos = (0, y)
            end_pos = (self.settings.screen_width, y)
            
            pygame.draw.line(self.screen, self.color, start_pos, end_pos)
            
            actual_row += 1
   
    def _blit_columns(self):
        actual_column = 0
        while actual_column < self.rows:
            x = int(self.settings.screen_width / self.rows * actual_column)
            
            start_pos = (x, 0)
            end_pos = (x, self.settings.screen_height)
            
            pygame.draw.line(self.screen, self.color, start_pos, end_pos)
            
            actual_column += 1
