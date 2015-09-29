"""creating a snow man """


import pygame
import sys

def snowman(screen, x, y):
    pygame.draw.ellipse(screen, white, [35 + x, 0 + y, 25, 25])
    pygame.draw.ellipse(screen, white, [23  +  x, 20  +  y, 50, 50])
    pygame.draw.ellipse(screen, white, [0  +  x, 65  +  y, 100, 100])

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)

size = [400, 500]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

while 1:
    for event in pygame.event.get():
	if event.type == pygame.QUIT:
	    sys.exit()
    screen.fill(black)
    
    snowman(screen, 10, 10)
    snowman(screen, 300, 10)
    snowman(screen, 10, 300)
    
    pygame.display.flip()
    clock.tick(60)
