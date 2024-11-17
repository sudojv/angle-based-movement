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
        self.screen_caption = 'Top Down Hero'
        self.screen_fps = 60
        # Hero settings
        self.hero_speed = 3
        ## Acceleration and attrition
        self.hero_max_acc = 1.0
        self.hero_min_acc = -1.0
        self.hero_acceleration = 0.05
        self.hero_attrition = 0.025
        ## Appearence
        self.hero_width = 25
        self.hero_height = 25
        self.hero_color = 'red'
        