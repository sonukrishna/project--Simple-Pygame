"""image """


import pygame
import sys
import random
clr1 = (0, 0, 0)
clr2 = (255, 255, 255)
clr3 = (155, 155, 155)

class Block(pygame.sprite.Sprite):
    def __init__(self, filename):
	pygame.sprite.Sprite.__init__(self)
	self.image = pygame.image.load(filename).convert()
	self.image.set_colorkey(clr1)
	self.rect = self.image.get_rect()
pygame.init()
size = [1000, 680]
screen = pygame.display.set_mode(size)
block_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()
for i in range(50):
    block = Block("ball.png")
    block.rect.x = random.randrange(size[0])
    block.rect.y = random.randrange(size[1])
    block_list.add(block)
    all_sprite_list.add(block)
player = Block("sss.png")
all_sprite_list.add(player)

clock = pygame.time.Clock()
score = 0
while 1:
    for event in pygame.event.get():
	if event.type == pygame.QUIT:
	    sts.exit()
    pos = pygame.mouse.get_pos()
    player.rect.x = pos[0]
    player.rect.y = pos[1]

    block_hit_list = pygame.sprite.spritecollide(player, block_list, True)
    for block in block_hit_list:
	score += 1
	print score
    all_sprite_list.draw(screen)
    clock.tick(60)
    pygame.display.flip()
