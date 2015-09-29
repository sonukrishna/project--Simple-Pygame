""" baby for the game """

import pygame
from baloon import Balloon


class Baby(Balloon):
    def __init__(self, screen):
        Balloon.__init__(self, screen)
        self.image = pygame.image.load('babe.jpg').convert()
