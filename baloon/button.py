"""creating a start page """


import pygame
import pygame.font


class Start(pygame.sprite.Sprite):
    def __init__(self, screen, x_pos, y_pos, settings, msg):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.settings = settings
        self.width, self.height = settings.button_width, settings.button_height
        self.x_pos, self.y_pos = x_pos, y_pos
        self.rect = pygame.Rect(x_pos, y_pos, self.width, self.height)
        self.font = pygame.font.SysFont('Ariel', 35)
        self.msg = msg
        self.prep_msg()

    def prep_msg(self):
        self.msg_image = self.font.render(self.msg, True,
                                          self.settings.button_text_color)
        # determine centere position of button
        self.msg_x = self.x_pos + (self.width -
                                   self.msg_image.get_width()) / 2
        self.msg_y = self.y_pos + (self.height -
                                   self.msg_image.get_height()) / 2

    def blitme(self):
        self.screen.fill(self.settings.button_bg, self.rect)
        self.screen.blit(self.msg_image, (self.msg_x, self.msg_y))
