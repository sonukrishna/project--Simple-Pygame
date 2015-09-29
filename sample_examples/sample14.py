"""moving sprites """


import pygame
import sys
import random
clr1 = (0, 0, 0)
clr2 = (255, 255, 255)
clr3 = (150, 150, 150)
class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
	pygame.sprite.Sprite.__init__(self)
	self.image = pygame.Surface([width, height])
	self.image.fill(color)
        self.rect = self.image.get_rect()
    def reset_pos(self):
	self.rect.y = random.randrange(-300, -20)
	self.rect.x = random.randrange(0, size[0])
    def update(self):
	self.rect.y += 1
	if self.rect.y > 410:
	    self.reset_pos()
class Player(Block):
    def update(self):
	pos = pygame.mouse.get_pos()
	self.rect.x = pos[0]
	self.rect.y = pos[1]
pygame.init()

size = [700, 400]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
block_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()
for i in range(100):
    block = Block(clr2, 20, 15)
    block.rect.x = random.randrange(size[0])
    block.rect.y = random.randrange(size[1])
    #add block to the list object
    block_list.add(block)
    all_sprite_list.add(block)
player = Player(clr3, 20, 15)
all_sprite_list.add(player)
score = 0
while 1:
    for event in pygame.event.get():
	if event.type == pygame.QUIT:
	    sys.exit()
    screen.fill(clr1)
    all_sprite_list.update()
    block_hit_list = pygame.sprite.spritecollide(player, block_list, True)
    for hit in block_hit_list:
	score += 1
	print score
	block.reset_pos()
    all_sprite_list.draw(screen)
    clock.tick(80)
    pygame.display.flip()
