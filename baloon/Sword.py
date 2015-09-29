"""creating a sword module """


import pygame


class Sword(pygame.sprite.Sprite):
    def __init__(self, screen, scoreboard_h):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.image.load('swrd.jpg').convert()
        self.image_w, self.image_h = self.image.get_size()
        self.x_pos = self.screen.get_width() / 2
        self.y_pos = self.image_h / 2 + scoreboard_h
        self.update_rect()
        self.grab_sword = False

    def blitme(self):
        draw_pos = self.image.get_rect().move(self.x_pos - self.image_w,
                                              self.y_pos - self.image_h / 2)
        self.screen.blit(self.image, draw_pos)

    def update_rect(self):
        self.rect = pygame.Rect(self.x_pos - self.image_w / 2,
                                self.y_pos - self.image_h / 2,
                                self.image_w, self.image_h)
