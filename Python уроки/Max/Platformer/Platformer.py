import time

import pygame
from pygame import *


pygame.init()

screen_width = 1024
screen_height = 800
screen = pygame.display.set_mode((screen_width,screen_height))

#Загрузка изображений
bg1 = pygame.image.load('images/background/bg1.jpg')
bg1 = pygame.transform.scale(bg1,(screen_width,screen_height))

player_img = pygame.image.load('images/player/player2.png')
player_img = pygame.transform.scale(player_img,(45,75))

rect = Rect(100,500,150,100)
rect2 = Rect(400,400,150,100)
obstacle_list = [rect,rect2]


player_rect = player_img.get_rect()
print(player_rect)

clock = pygame.time.Clock()

jump_counter = -30
make_jump = False
gravity = 10
in_air = True




def keys():
    global make_jump
    keys = pygame.key.get_pressed()
    if keys[K_d]:
        player_rect.x += 5

    if keys[K_a]:
        player_rect.x -= 5
    if keys[K_w]:
        player_rect.y -= 5
    if keys[K_s]:
        player_rect.y += 5

    if keys[K_SPACE]:
        make_jump = True


lst = []

def jump():
    global jump_counter, make_jump, player_rect, gravity, in_air
    if jump_counter <= 31:
        gravity = 0
        player_rect.y += jump_counter / 2
        jump_counter += 1


    else:
        make_jump = False
        jump_counter = -30
        gravity = 10
        in_air = True


def check_collision():
    global gravity, in_air, make_jump , jump_counter
    for barrier in obstacle_list:
        pygame.draw.rect(screen, (0, 255, 0), barrier)
        if player_rect.colliderect(barrier):
            make_jump = False
            jump_counter = -30
            gravity = 0
            # in_air = False


run = True
def run_game():
    global make_jump, player_rect , gravity

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                # print('Любая клавиша нажата')
                print(pygame.key.name(event.key))
        keys()

        screen.blit(bg1,(0,0))
        screen.blit(player_img,(player_rect.x,player_rect.y))
        # pygame.draw.rect(screen,(200,0,0),player_rect)
        if make_jump == True:
            jump()

        check_collision()
        # print(player_rect.y)


        player_rect.y += gravity

        pygame.display.update()
        clock.tick(30)

run_game()
