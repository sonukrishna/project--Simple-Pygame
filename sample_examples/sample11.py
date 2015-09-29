"""graw rectangles recursively """

import pygame
import sys
clr1 = (0, 0, 0)
clr2 = (255, 255, 255)

def recursive(x, y, width, height):
    pygame.draw.rect(screen, clr2, [x, y, width, height], 2)
    if width > 14:
	x = width * .1
	y = height * .1
        width = width * .8
	height = height * .8
	recursive(x, y, width, height)

pygame.init()
size = [720, 480]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
while 1:
    for event in pygame.event.get():
	if event.type == pygame.QUIT:
	    sys.exit()
    screen.fill(clr1)
    recursive(0, 0, 700, 500)
    pygame.display.flip()
    clock.tick(60)
