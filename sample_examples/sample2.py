import pygame
import sys

pygame.init()

color = (255, 255, 255)
color1 = (0, 255, 255)
color2 = (255, 0, 255)
color3 = (0, 0, 0)
color4 = (255, 255, 0)

size = [720, 480]
screen = pygame.display.set_mode(size)

pygame.display.set_caption('sample 2')

clock = pygame.time.Clock()
while 1:
     for event in pygame.event.get():
	 if event.type == pygame.QUIT:
	     sys.exit()
     screen.fill(color1)
     pygame.draw.line(screen, color2, [0, 0], [50, 30], 5)
     pygame.draw.lines(screen, color2, False, [[0, 80], [50, 90], [150,90], [220, 30]], 8)
     pygame.draw.aaline(screen, color3, [0,50], [50, 30])
     pygame.draw.rect(screen, color4, [300, 10, 50, 20], 4)
     pygame.draw.ellipse(screen, color4, [500, 110, 250, 220])
     pygame.draw.polygon(screen, color2, [[100, 100], [0, 200], [200,200]], 4)
     pygame.draw.circle(screen, color3, [50, 250], 40)
     pygame.display.flip()
     clock.tick(60)
