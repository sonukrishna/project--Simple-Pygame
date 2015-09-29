"""levels """



import pygame
import random

clr1 = (0, 0, 0)
clr2 = (255, 255, 255)
clr3 = (200, 100, 0)


class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
pygame.init()
size = [720, 480]
screen = pygame.display.set_mode(size)

block_list = pygame.sprite.Group() #list of sprites
all_sprites_list = pygame.sprite.Group()

for i in range(60):
    block = Block(clr2, 20, 15)
    block.rect.x = random.randrange(size[0])
    block.rect.y = random.randrange(size[1])
    block_list.add(block)
    all_sprites_list.add(block)

player = Block(clr3, 20, 15)
all_sprites_list.add(player)

clock = pygame.time.Clock()
score = 0
level = 1
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(clr1)
    pos = pygame.mouse.get_pos()
    player.rect.x = pos[0]
    player.rect.y = pos[1]

    # what if somethin hit
    block_hit_list = pygame.sprite.spritecollide(player, block_list, True)
    for block in block_hit_list:
        score += 1
        print score
    if len(block_list) == 0:
	level += 1
	for i in range(level * 60):
	    block.rect.x = random.randrange(size[0])
	    block.rect.y = random.randrange(size[1])
	    block_list.add(block)
            all_sprites_list.add(block)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(64)
       



