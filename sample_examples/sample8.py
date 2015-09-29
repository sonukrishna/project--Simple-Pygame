"""baground music """

import pygame
import sys
pygame.init()

clr1 = (0, 0, 0)
clr2 = (255, 255, 255)

size = [200, 200]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
	
pygame.mixer.music.load('1.mp3')
pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
pygame.mixer.music.play()

while 1:
    for event in pygame.event.get():
	if event.type == pygame.QUIT:
	    sys.exit()
	elif event.type == pygame.constants.USEREVENT:
	    pygame.mixer.music.load('2.mp3')
	    pygame.mixer.music.play()
    screen.fill(clr2)
    pygame.display.flip()
    clock.tick(60)
