class Settings:
    '''Class to manage game settings'''
    def __init__(self):
        '''Initialize the game settings'''
        # Screen settings
        self.screen_width = 640
        self.screen_height = 480
        self.screen_size = (
            self.screen_width, self.screen_height
        )
        self.screen_color = 'black'
        self.screen_caption = 'PyGame'
        self.screen_fps = 60