import pygame
import sys
pygame.init()

color = (0, 0, 0)
color1 = (255, 255, 255)
color2 = (0, 255, 10)
size = (720, 480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Rotate_shift")
clock = pygame.time.Clock()
degree = 0

while 1:
    for event in pygame.event.get():
	if event.type == pygame.QUIT:
     	    sys.exit()
    
    screen.fill(color)
    pygame.draw.line(screen, color1, [100,50], [200,50])
    pygame.draw.line(screen, color1, [100,50], [100,150])
    font = pygame.font.SysFont("Calibri", 34, True, False)
    text = font.render("My naee is tht", True, color1)
    text = pygame.transform.rotate(text, 90)
    screen.blit(text, [0, 0])

    text = font.render("my age is thae", True, color2)
    text = pygame.transform.rotate(text, 180)
    screen.blit(text, [200, 0])

    text = font.render("what i type next", True, color2)
    text = pygame.transform.flip(text, False, True)
    screen.blit(text, [100, 20])
    

    text = font.render("sOnu", True, color1)
    text = pygame.transform.rotate(text, degree)
    degree += 5 
    screen.blit(text, [100, 50])

    pygame.display.flip()

    clock.tick(60)
