"""keyboard inputs """

import pygame
import sys

black = (0, 0, 0)
white = (255,255, 255)
grn = (0, 255, 0)
red = (255, 0, 0)

def draw(screen, x, y):
    pygame.draw.ellipse(screen, white, [1 + x, y, 10, 10], 2)
    pygame.draw.line(screen, white, [5  +  x, 17  +  y], [10  +  x, 27  +  y], 2)
    pygame.draw.line(screen, black, [5  +  x, 17  +  y], [x, 27  +  y], 2)
    pygame.draw.line(screen, red, [5  +  x, 17  +  y], [5  +  x, 7  +  y], 2)
    pygame.draw.line(screen, red, [5  +  x, 7  +  y], [9  +  x, 17  +  y], 2)
    pygame.draw.line(screen, red, [5  +  x, 7  +  y], [1  +  x, 17  +  y], 2)

pygame.init()
size = [720, 480]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

pygame.mouse.set_visible(0)

xs = 0
ys = 0

xp = 10
yp = 10

while 1:
    for event in pygame.event.get():
	if event.type == pygame.QUIT:
	    sys.exit()
        elif event.type == pygame.KEYDOWN:
	    if event.key == pygame.K_LEFT:
		xs = -3
	    elif event.key == pygame.K_RIGHT:
		xs = 3
	    elif event.key == pygame.K_UP:
		ys = -3
	    elif event.key == pygame.K_DOWN:
		ys = 3
	elif event.type == pygame.KEYUP:
	    if event.key == pygame.K_LEFT:
		xs = 0
	    elif event.key == pygame.K_RIGHT:
		xs = 0
	    elif event.key == pygame.K_UP:
		ys = 0
	    elif event.key == pygame.K_DOWN:
		ys = 0

    xp = xp + xs
    yp = yp + ys

    screen.fill(grn)

    draw(screen, xp, yp)
    pygame.display.flip()
    clock.tick(30)
