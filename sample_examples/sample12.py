""" time count """

import pygame
import sys
pygame.init()

clr1 = (0, 0, 0)
clr2 = (255, 255, 255)
clr3 = (155, 155, 155)
clr4 = (75, 75, 75)

size = [720, 480]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
frame_count = 0
frame_rate = 60
start_count = 90
while 1:
     for event in pygame.event.get():
	 if event.type == pygame.QUIT:
	     sys.exit()
     screen.fill(clr1)
     total_sec = frame_count // frame_rate
     minutes = total_sec // 60
     seconds = total_sec % 60
     output_string  =  "Time: {0:02}:{1:02}".format(minutes, seconds)
     text = font.render(output_string, True, clr2)
     total_sec = start_count - (frame_count // frame_rate)
     screen.blit(text, [250, 250])
     if total_sec < 0:
	 total_sec = 0
     minutes = total_sec // 60
     seconds = total_sec % 60
     output_str = "Time: {0:02}:{1:02}".format(minutes, seconds)
     text = font.render(output_str, True, clr3)
     screen.blit(text, [250, 280])
     frame_count += 1
     
     pygame.display.flip()
     clock.tick(frame_count)
