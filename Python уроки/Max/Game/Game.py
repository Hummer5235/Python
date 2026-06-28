import pygame
from pygame import *

W = 800
H = 600
screen = pygame.display.set_mode((W,H))

pygame.display.set_caption('Game')

clock = pygame.time.Clock()
player_image = pygame.image.load('player.png')
player_image = pygame.transform.scale(player_image,(80,80))
player_rect = player_image.get_rect(center = (W//2,H//2))
player_direction = 1

enemy_image = pygame.image.load('enemy.png')
enemy_image = pygame.transform.scale(enemy_image,(80,80))
enemy_rect = enemy_image.get_rect(center = (W//2,H//2))


def check_keys():
    global player_direction
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if player_rect.y > 0:
            player_rect.y -= 5

    if keys[pygame.K_s]:
        if player_rect.y + player_image.get_height() < H:
            player_rect.y += 5
    if keys[pygame.K_a]:
        if player_rect.x > 0:
            player_rect.x -= 5
            player_direction = False
    if keys[pygame.K_d]:
        if player_rect.x + player_image.get_width() < W:
            player_rect.x += 5
            player_direction = True






while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    check_keys()
    screen.fill((0,0,0))
    screen.blit(pygame.transform.flip(player_image,player_direction,False),player_rect)
    screen.blit(enemy_image,enemy_rect)
    pygame.display.update()

    clock.tick(30)





