"""game over """



import pygame
import sys
pygame.init()

clr1 = (0, 0, 0)
clr2 = (255, 255, 255)

size = [400, 400]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
game = False
x_pos = 50
y_pos = 50
x_spd = 5
y_spd = 5
font = pygame.font.Font(None, 40)
while 1:
    for event in pygame.event.get():
	if event.type == pygame.QUIT:
	    sys.exit()
	elif event.type == pygame.MOUSEBUTTONDOWN:
	    game = True
    if not game:
	x_pos += x_spd
	y_pos += y_spd

	if x_pos > 400 or x_pos < 0:
	    x_spd = -x_spd
	if y_pos > 400 or y_pos < 0:
	    y_spd = -y_spd
    screen.fill(clr1)
    pygame.draw.rect(screen, clr2, [x_pos, y_pos, 50, 50], 2)
    
    if game:
	text = font.render('Game Over', True, clr2)
        text_rect = text.get_rect()
	text_x = screen.get_width()/2 - text_rect.width/2
	text_y = screen.get_height()/2 - text_rect.height/2
	screen.blit(text, [text_x, text_y])
    else:
	text = font.render("click to end the game", True, clr2)
        text_rect = text.get_rect()
	text_x = screen.get_width() / 2 - text_rect.width / 2
	text_y = screen.get_height() / 2 - text_rect.height / 2
	screen.blit(text, [text_x, text_y])
    clock.tick(60)
    pygame.display.flip()


	 
