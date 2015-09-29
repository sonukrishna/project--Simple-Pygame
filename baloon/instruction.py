"""small description of game """


import pygame
import pygame.font
class Instruction(pygame.sprite.Sprite):
    def __init__(self, screen, settings):
	pygame.sprite.Sprite.__init__(self)
	self.screen = screen
	self.settings = settings

	self.text_color = (0, 0, 0)
	self.font = pygame.font.SysFont('Nimbus Mono L', 24)

	# our description
	self.lines = ["this game is about to pop the balloons"]
	self.lines.append("double click/press mouse help to grab the sword")
	self.lines.append("if you kills a baby missed balloon increased by 10")
	self.lines.append("if missed balloon greater than 69, game over")
	self.lines.append("THANK YOU")

#	self.prep_msg()

	def prep_msg(self):
	    y_pos = self.settings.screen_height / 2 + \
		    self.settings.button_height
#	    self.images, self.msg_x, self.msg_y = [], [], []
	    for  line in self.lines:
		self.images = self.font.render(line, True, self.text_color)
#		self.msg_x.append(self.settings.screen_width / 2 - \
#				  self.font.size(line)[0] / 2) 
#		self.msg_y.append(y_pos + index* self.font.size(line)[1] / 2)

	def blitme(self):
	    self.prep_msg()
	    self.screen.blit(line, (100, y_pos))	
