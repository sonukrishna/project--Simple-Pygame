""" instruction screen """
import pygame
import sys
pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

size = [720, 480]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("instruction screen")
clock = pygame.time.Clock()

x_pos = 50
y_pos = 50

x_spd = 5
y_spd = 5

font = pygame.font.Font(None, 36)
instructions = True
count = 1

while 1 and instructions:
    for event in pygame.event.get():
	if event.type == pygame.QUIT:
	    sys.exit()
	if event.type == pygame.MOUSEBUTTONDOWN:
	    count += 1
	    if count == 3:
		instructions = False
    screen.fill(black)
    if instructions == 1:
	text = font.render("Instructions", True, white)
	screen.blit(text, [10, 10])
	
	text = font.render("page1", True, white)
	screen.blit(text, [10, 40])

    if instructions == 2:
	text = font.render("this programs jumps a rectangle", True, white)
	screen.blit(text, [10, 10])
	text = font.render("page2", True, white)
	screen.blit(text, [10, 40])
   
    clock.tick(60)
    pygame.display.flip()

while 1:
    for event in pygame.event.get():
	if event.type == pygame.QUIT:
	    sys.exit()

    screen.fill(black)
    pygame.draw.rect(screen, white, [x_pos, y_pos, 50, 50])
    x_pos += x_spd
    y_pos += y_spd

    if x_pos > 720 or x_pos < 0:
	x_pos = -(x_pos)
    if y_pos > 480 or y_pos < 0:
	y_pos = -(y_pos)
    

    clock.tick(60) 
    pygame.display.flip()
