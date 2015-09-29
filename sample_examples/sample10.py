"""radar00 """

import math
import pygame
import sys
pygame.init()

clr1 = (0, 0, 0)
clr2 = (255, 255, 255)
clr3 = (155, 251, 0)
clr4 = (10, 200, 155)
size = [720, 480]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
angle = 0
pi = 3.1415
while 1:
    for event in pygame.event.get():
	if event.type == pygame.QUIT:
	    sys.exit()
    screen.fill(clr1)
    box = [20, 20, 250, 250]
    pygame.draw.ellipse(screen, clr2, box, 3)
    pygame.draw.rect(screen, clr3, box, 3)
    x = 125 * math.sin(angle) + 145
    y = 125 * math.cos(angle) + 145
    pygame.draw.line(screen, clr4, [145, 145], [x, y], 2)
    angle += 0.03
    if angle > 2 * pi:
	angle = angle - 2 * pi
    pygame.display.flip()
    clock.tick(60)
