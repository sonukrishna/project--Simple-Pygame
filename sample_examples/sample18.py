""" game class """


import pygame
import random

clr1 = (0, 0, 0)
clr2 = (255, 255, 255)
clr3 = (0, 255, 0)
clr4 = (255, 255, 0)

size = [700, 500]

class Block(pygame.sprite.Sprite):
    def __init__(self):
	pygame.sprite.Sprite.__init__(self)
	self.image = pygame.Surface([20, 20])
	self.image.fill(clr1)
	self.rect = self.image.get_rect()
    def reset_pos(self):
	self.rect.y = random.randrange(-300, -20)
	self.rect.x = random.randrange(size[0])
    def update(self):
	self.rect.y += 1
	if self.rect.y > size[1] + self.rect.height:
	    self.reset_pos()

class Player(pygame.sprite.Sprite):
    def __init__(self):
	pygame.sprite.Sprite.__init__(self)
	self.image = pygame.Surface([20, 20])
	self.image.fill(clr3)
	self.rect = self.image.get_rect()

    def update(self):
	pos = pygame.mouse.get_pos()
	self.rect.x = pos[0]
	self.rect.y = pos[1]
class Game(object):
    def __init__(self):
	self.score = 0
	self.game_over = False
	self.block_list = pygame.sprite.Group()
	self.all_sprite_list = pygame.sprite.Group()
	for i in range(50):
	    block = Block()
	    block.rect.x = random.randrange(size[0])
	    block.rect.y = random.randrange(size[1])

	    self.block_list.add(block)
	    self.all_sprite_list.add(block)
	self.player = Player()
	self.all_sprite_list.add(self.player)
    def process_events(self):
	for event in pygame.event.get():
	    if event.type == pygame.QUIT:
		return True
	    if event.type == pygame.MOUSEBUTTONDOWN:
		if self.game_over:
		    self.__init__()
	return False

    def run_logic(self):
	if not self.game_over:
	    self.all_sprite_list.update()
	    block_hit_list = pygame.sprite.spritecollide(self.player, block_list, True)
	    for blocks in block_hit_list:
		self.score += 1
		print self.score	
	    if len(self.block_list) == 0:
		self.game_over = True

    def display_frame(self, screen):
	screen.fill(clr1)
	if self.game_over:
	    font = pygame.font.SysFont("serif", 34)
	    text = font.render("Game Over", True, clr2)
	    x_pos = (size[0] // 2) - (text.get_width() // 2)
	    y_pos = (size[1] // 2) - (text.get_height() // 2)
	    screen.blit(text, [x_pos, y_pos])
	if not self.game_over:
	    self.all_sprite_list.draw(screen)
	pygame.display.flip()

def main():
    pygame.init()
  #  size = [size[0], size[1]]
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(True)
    game = Game()
    done = False
    while not done:
	done = game.process_events()
	game.run_logic
	game.display_frame(screen)
	clock.tick(60)
	

main()

