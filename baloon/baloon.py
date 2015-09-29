"""creating a baloon module """


import pygame
import random


class Balloon(pygame.sprite.Sprite):
    """this class represents the baloons """
    def __init__(self, screen):
        """Constructor function """
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.image.load('bln4.jpg').convert()
        self.image_w, self.image_h = self.image.get_size()
        self.speed = 0.3
        #balloon positions
        self.x_pos = random.randint(self.image_w / 2,
                                    self.screen.get_width() -
                                    self.image_w / 2)
        self.y_pos = self.screen.get_height() + self.image_h / 2
        #make a rect object
        self.update_rect()

    def update(self, time_changed):
        self.y_pos -= self.speed * time_changed
        self.update_rect()

    def blitme(self):
        draw_pos = self.image.get_rect().move(self.x_pos -
                                              self.image_w / 2,
                                              self.y_pos -
                                              self.image_h / 2)
        self.screen.blit(self.image, draw_pos)

    def update_rect(self):
        """it make rectangle objects """
        self.rect = pygame.Rect(self.x_pos - self.image_w / 2,
                                self.y_pos - self.image_h / 2,
                                self.image_w, self.image_h)
