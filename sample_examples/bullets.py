"""how to fire a bulllete """


import pygame
import random
import sys

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

class Block(pygame.sprite.Sprite):
    def __init__(self, color):
	pygame.sprite.Sprite.__init__(self)
	self.image = pygame.Surface([20,10])
	self.image.fill(color)
	
	self.rect = self.image.get_rect()

class Player(pygame.sprite.Sprite):
    def __init__(self):
	pygame.sprite.Sprite.__init__(self)
	self.image = pygame.Surface([20, 10])
	self.image.fill(blue)
	self.rect = self.image.get_rect()
    def update(self):
	pos = pygame.mouse.get_pos()
	self.rect.x = pos[0]

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
	pygame.sprite.Sprite.__init__(self)
	self.image = pygame.Surface([4, 10])
	self.image.fill(blue)
	self.rect = self.image.get_rect()

    def update(self):
	self.rect.y -= 3

pygame.init()

size = [700, 400]
screen = pygame.display.set_mode(size)

block_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()

for i in range(50):
    block = Block(black)
    block.rect.x = random.randrange(size[0])
    block.rect.y = random.randrange(350)
    block_list.add(block)
    all_sprite_list.add(block)
player = Player()
all_sprite_list.add(player)
clock = pygame.time.Clock()
score = 0
player.rect.y = 370
while 1:
    for event in pygame.event.get():
	if event.type == pygame.QUIT:
	    sys.exit()
	elif event.type == pygame.MOUSEBUTTONDOWN:
	    bullet = Bullet()
	    bullet.rect.x = player.rect.x
	    bullet.rect.y = player.rect.y
	    all_sprite_list.add(bullet)
	    bullet_list.add(bullet)
	    bullet.update()
    all_sprite_list.update()
    for bullet in bullet_list:
	block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)
	for block in block_list:
	    bullet_list.remove(bullet)
	    all_sprite_list.remove(bullet)
            score += 1
	    print score
	if bullet.rect.y < -5:
	    bullet_list.remove(bullet)
	    all_sprite_list.remove(bullet)
    screen.fill(white)
    all_sprite_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)
