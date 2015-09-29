""" A simple py game """


import pygame
import sys
from baloon import Balloon
from Sword import Sword
from Scorecard import Scoreboard
from button import Start
from settings import Settings
from baby import Baby
from random import random
#from instruction import Instruction
#initialize game
pygame.init()


def run_game():
#    bg_color = (255, 255, 255)
    settings = Settings()
#    size = [1080, 620]
    screen = pygame.display.set_mode(settings.size)
#    scoreboard_h = 50
#    score_inc = 10
    clock = pygame.time.Clock()
    #Create our first balloon
#    first_bal = Balloon(screen)
    scoreboard = Scoreboard(screen, settings)
#    instructions = Instruction(screen, settings)
#    baloon_list = [Balloon(screen)]
    my_sword = Sword(screen, settings.scoreboard_h)
    play_game = Start(screen, settings.size[0] / 2 -
                      settings.button_width / 2,
                      settings.size[1] / 2 - settings.button_height / 2,
                      settings, "Play Game")
    game_over = Start(screen, play_game.x_pos, play_game.y_pos -
                      2 * settings.button_height, settings, "Game Over")
#    instructions = Instruction(screen, settings)
    baloon_list = []
    baby_list = []
    spawn_baloon(screen, settings, baloon_list, baby_list)
    spawn_babies(screen, baby_list)
    #main loop
    while 1:
        time_changed = clock.tick(50)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        check_events(my_sword, scoreboard, settings, play_game,
                     mouse_x, mouse_y, baloon_list)
        #redraw the screen
        screen.fill(settings.bg_color)
        if settings.activate:
            update_sword(my_sword, mouse_x, mouse_y, settings)
            #update the swords positions
            check_baloons(baloon_list, baby_list, my_sword, scoreboard, screen,
                          settings, time_changed)
            check_babies(baby_list, my_sword, scoreboard, screen,
                         settings, time_changed)
            if len(baloon_list) == 0:
                settings.baloon_speed *= settings.speed_factor
                settings.baby_ratio *= settings.speed_factor
                release_next(screen, baby_list, settings, baloon_list)
        else:
            play_game.blitme()
#	    if settings.game_played:
#		instructions.blitme()
            if settings.game_played > 0:
                game_over.blitme()
        #scorecard
        scoreboard.blitme()
#	my_button.blitme()
        #draw our balloon to screen
#	first_bal.blitme()
        pygame.display.flip()


def release_next(screen, baby_list, settings, baloon_list):
    for x in range(0, settings.batch_size):
        spawn_baloon(screen, settings, baloon_list, baby_list)


def check_baloons(baloon_list, baby_list, my_sword, scoreboard,
                  screen, settings, time_changed):
    for baloons in baloon_list:
        baloons.update(time_changed)
      #  print "baloon positions :", baloons.y_pos
       # baloons.blitme()
        if baloons.rect.colliderect(my_sword.rect):
            pop_baloon(scoreboard, settings, baloons, baloon_list)
        if baloons.y_pos < -baloons.image_h / 2 + settings.scoreboard_h:
            miss_baloon(scoreboard, baloons, baloon_list)
            spawn_baloon(screen, settings, baloon_list, baby_list)
        baloons.blitme()
    if scoreboard.baloons_missed > 69:
        settings.activate = False
        settings.game_played += 1


def check_babies(baby_list, my_sword, scoreboard, screen,
                 settings, time_changed):
    """define the babies """
    for babe in baby_list:
        babe.update(time_changed)
        if babe.rect.colliderect(my_sword.rect):
            kill_babe(scoreboard, settings, baby_list, babe)
        if babe.y_pos < -babe.image_h / 2 + settings.scoreboard_h:
            spare_babe(scoreboard, settings, baby_list, babe)
            spawn_babies(screen, baby_list)
        babe.blitme()


def update_sword(my_sword, mouse_x, mouse_y, settings):
    my_sword.x_pos = mouse_x
    if my_sword.grab_sword:
        my_sword.y_pos = mouse_y
    else:
        my_sword.y_pos = my_sword.image_h / 2 + settings.scoreboard_h
    my_sword.update_rect()
    my_sword.blitme()


def pop_baloon(scoreboard, settings, baloons, baloon_list):
    scoreboard.baloons_poped += 1
    scoreboard.scored += settings.score_inc
    baloon_list.remove(baloons)
    if scoreboard.baloons_poped % settings.pops == 0:
        settings.batch_size += 1


def miss_baloon(scoreboard, baloons, baloon_list):
    scoreboard.baloons_missed += 1
    baloon_list.remove(baloons)


def spare_babe(scoreboard, settings, baby_list, babe):
    """babys escaped """
    scoreboard.babe_spare += 1
    scoreboard.scored += settings.baby_spare_factor * settings.score_inc
    baby_list.remove(babe)


def kill_babe(scoreboard, settings, baby_list, babe):
    """babys killed """
    scoreboard.babe_killed += 1
    scoreboard.baloons_missed += 10
#    babe = pygame.transform.rotate(babies.image, 90)
    baby_list.remove(babe)


def spawn_baloon(screen, settings, baloon_list, baby_list):
    baloon_list.append(Balloon(screen))
    if random() < settings.baby_ratio:
        spawn_babies(screen, baby_list)


def spawn_babies(screen, baby_list):
    baby_list.append(Baby(screen))


def check_events(my_sword, scoreboard, settings, play_game,
                 mouse_x, mouse_y, baloon_list):
    """this function check events occured """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if my_sword.rect.collidepoint(mouse_x, mouse_y):
                my_sword.grab_sword = True
            if play_game.rect.collidepoint(mouse_x, mouse_y):
                del baloon_list[:]
                scoreboard.initialize_status()
                settings.initialize()
                settings.activate = True
        if event.type == pygame.MOUSEBUTTONUP:
            my_sword.grab_sword = False


run_game()
