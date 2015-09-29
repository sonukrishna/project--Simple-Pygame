"""this module help to create more buttons """


class Settings():
    def __init__(self):
        self.screen_width, self.screen_height = 1080, 620
        self.bg_color = (255, 255, 255)
        self.scoreboard_h = 50
        self.button_width, self.button_height = 250, 50
        self.size = [1080, 620]
        self.button_bg = (0, 163, 0)
        self.button_text_color = (205, 205, 205)
        self.initialize()
        #play button condition
        self.activate = False
        #game over conditions
        self.max_miss = 69
        self.game_played = 0

    def initialize(self):
        self.baloon_speed = 0.2
        self.speed_factor = 1.05
        self.score_inc = 10
        self.bln_released = 1
        self.batch_size = 1
        self.pops = 5
        self.baby_ratio = 0.10
        self.baby_spare = 0
        self.baby_spare_factor = 3
