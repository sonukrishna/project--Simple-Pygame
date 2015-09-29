import os, sys
import pygame
from pygame.locals import*

if not pygame.font:
    print 'Warning,no font found'
if not pygame.mixer:
    print 'Warning, no sound is found'

def ld_image(name,colorkey=None):
    fullname = os.path.join('data',name)
    image = pygame.image.load(fullname)
    image = image.convert()
    if colorkey is not None:
	if colorkey is -1:
	    colorkey = image.get_at((0,0))
	image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()
def ld_sound(name):
    class NoneSound:
	def play(self):
	    pass
    if not pygame.mixer:
	return NoneSound()
    fullname = os.path.join("data",name)
    sound = pygame.mixer.Sound(fullname)
    return sound
class Fist(pygame.sprite.Sprite):
    """movement of fist on the screen """
    def __init__(self):
	pygame.sprite.Sprite.__init__(self)
	self.image,self.rect = ld_image('sss.png',-1)
	self.punching = 0
    def update(self):
	"""move the fist based on the mouse position """
	pos = pygame.mouse.get_pos()
	self.rect.midtop = pos
	if self.punching:
	    self.rect.move_ip(5, 10)
    def punch(self,target):
	"""returns true if fist collide with target """
	if not self.punching:
	    self.punching = 1
	    hit = self.rect.inflate(-5, -5)
	    return hit.colliderect(target.rect)
    def unpunch(self):
	"""pull back the fist """
	self.punching = 0
class Chimp(pygame.sprite.Sprite):
    """ move the monkey on the surface """
    def __init__(self):
	pygame.sprite.Sprite.__init__(self)
	self.image, self.rect = ld_image('download.jpg',-1)
	screen = pygame.display.get_surface()
	self.area = screen.get_rect()
	self.rect.topleft = 10, 10
	self.move = 9
	self.dizzy = 0
    def update(self):
	"""walks or spins """
	if self.dizzy:
	    self.spins()
	else:
	    self.walks()
    def walks(self):
	"""move the monkey across the screen """
	newpos = self.rect.move((self.move, 0))
#	if not self.area.contains(newpos):
	if self.rect.left < self.area.left or \
	    self.rect.right > self.area.right:
	    self.move = -self.move
	    newpos = self.rect.move((self.move,0))	
	    self.image = pygame.transform.flip(self.image,1,0)
	self.rect = newpos
    def spins(self):
	"""spins the image """
	center = self.rect.center
	self.dizzy += 12
	if self.dizzy >= 360:
	    self.dizzy = 0
	    self.image =self.original
	else:
	    rotate = pygame.transform.rotate
	    self.image = rotate(self.original, self.dizzy)
	self.rect =self.image.get_rect(center = center)
    def punched(self):
	"""cuase the monkey to start spinning """
	if not self.dizzy:
	    self.dizzy = 1
	    self.original = self.image

def main():
    """this function initialize everything and runs in loop """
# initializing    
    pygame.init()
    screen = pygame.display.set_mode((720,380))
    pygame.display.set_caption('Sonus Game')
    pygame.mouse.set_visible(0)

#Create the background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

#Put text on the background, centerd
    if pygame.font:
	font = pygame.font.Font(None, 40)
	text = font.render("athra is the chimp,and win $$$",1,(10,10,10))
	textpos = text.get_rect(centerx=background.get_width()/2)
	background.blit(text, textpos)
#Display the background
    screen.blit(background,(0,0))
    pygame.display.flip()

#Prepare game object
    whiff_sound = ld_sound('1.mp3')
    punch_sound = ld_sound('2.wav')
    chimp = Chimp()
    fist = Fist()
    allstripes = pygame.sprite.RenderPlain((fist, chimp))
    clock = pygame.time.Clock()

#Main loop
    while 1:
	clock.tick(240)

    #Handle input objects
	for event in pygame.event.get():
	    if event.type == QUIT:
		return
	    elif event.type == KEYDOWN and event.key == K_ESCAPE:
		return
	    elif event.type == MOUSEBUTTONDOWN:
		if fist.punch(chimp):
		    punch_sound.play()
		    chimp.punched()
		else:
		    whiff_sound.play()
	    elif event.type == MOUSEBUTTONUP:
		fist.unpunch()
        allstripes.update()
    #Draw entire scene
    	screen.blit(background, (0,0))
	allstripes.draw(screen)
	pygame.display.flip()
main()
