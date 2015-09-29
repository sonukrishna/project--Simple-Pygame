"""grid """


import pygame
import sys

a = [0, 0, 0]
b = [255, 255, 255]
c = [255, 255, 250]
d = [200, 200, 150]

w = 20
h = 20
mar = 5
grid = []
for i in range(10):
    grid.append([])
    for j in range(10):
	grid[i].append(0)
grid[1][5] = 1
pygame.init()
size =[255, 255]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

while 1:
    for event in pygame.event.get():
	if event.type == pygame.QUIT:
	    sys.exit()
	elif event.type ==pygame.MOUSEBUTTONDOWN:
	    pos =pygame.mouse.get_pos()
	    col = pos[0] // (w + mar)
	    raw = pos[1] // (h + mar)
            grid[raw][col] = 1
	    print("Click", pos, "grid coordinates: ", raw, col)
    screen.fill(a)
    for raw in range(10):
	for col in range(10):
	    color = b
	    if grid[raw][col] == 1:
		color = d 
		pygame.draw.rect(screen, color, [(mar + w) * col +mar,
		                    (mar + h) * raw + mar, w, h])
    pygame.display.flip()
    clock.tick(20)
