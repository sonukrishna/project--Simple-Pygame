"""the scoreboard module """


import pygame
import pygame.font


class Scoreboard(pygame.sprite.Sprite):
    """score board for our game """
    def __init__(self, screen, settings):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.settings = settings
#	self.baloons_poped = 0
#	self.baloons_missed = 0
#       self.scored = 0
        #set diemensions
        self.sb_height, self.sb_width = settings.scoreboard_h, self.screen.get_width()
        self.rect = pygame.Rect(0, 0, self.sb_width, self.sb_height)
        self.bg_clr = (100, 100, 110)
        self.text_clr = (0, 0, 0)
        self.font = pygame.font.SysFont('Calibri', 36)
        #positions for individual scoring elements
        self.x_pop_pos, self.y_pop_pos = 20.0, 10.0
        self.x_miss_pos, self.y_miss_pos = 450.0, 10.0
        self.x_score, self.y_score = 850.0, 10.0
        self.initialize_status()

    def initialize_status(self):
        self.baloons_poped = 0
        self.baloons_missed = 0
        self.scored = 0
        self.babe_spare = 0
        self.babe_killed = 0

    def scores(self):
        self.pop_string = "No.of popped :" + str(self.baloons_poped)
        self.pop_image = self.font.render(self.pop_string,
                                          True, self.text_clr)
        self.miss_string = "No.of Missed :" + str(self.baloons_missed)
        self.miss_image = self.font.render(self.miss_string,
                                           True, self.text_clr)
        self.score_string = "Total Score :" + str(self.scored)
        self.score_image = self.font.render(self.score_string,
                                            True, self.text_clr)

    def blitme(self):
        self.scores()
        self.screen.fill(self.bg_clr, self.rect)
        self.screen.blit(self.pop_image, (self.x_pop_pos,
                                          self.y_pop_pos))
        self.screen.blit(self.miss_image, (self.x_miss_pos,
                                           self.y_miss_pos))
        self.screen.blit(self.score_image, (self.x_score,
                                            self.y_score))
