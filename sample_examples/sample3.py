"""multiple objects """

import pygame
import random
import sys
res = []
pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
color1 = (144, 145, 255)
color2 = (255, 200,0)

size = [720, 480]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("snow animation")

clock = pygame.time.Clock()
for i in range(50):
    x = random.randrange(0, 720)
    y = random.randrange(0, 480)
    res.append([x, y])
while 1:
    for event in pygame.event.get():
	if event.type == pygame.QUIT:
	    sys.exit()
    for i in range(len(res)):
	pygame.draw.circle(screen, white, res[i], 1)
	res[i][1] += 20 
	if res[i][1] > 480:
	    y = random.randrange(-50, -30)
	    res[i][1] = y
	    x = random.randrange(0, 720)
	    res[i][0] = x
    pygame.display.flip()
    clock.tick(25)
    
        
