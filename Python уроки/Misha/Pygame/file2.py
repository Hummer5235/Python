# -*- coding: utf-8 -*-

import pygame
pygame.init()

W, H = 800, 600
WHITE = (255, 255, 255)
BLACK = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)



screen = pygame.display.set_mode((W,H)) #Создание окна
pygame.display.set_caption('Мое окно')
pygame.display.set_icon(pygame.image.load('Icon1.png'))



clock = pygame.time.Clock() # создай экз часы
FPS = 60
x = 400
y = 300
speed = 5

left = False
right = False
up = False
down = False


i = 0
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN: #Клавиша нажата

            if event.key == pygame.K_DOWN:
                down = True
            if event.key == pygame.K_UP:
                up = True
            if event.key == pygame.K_LEFT:
                left = True
            if event.key == pygame.K_RIGHT:
                right = True
        if event.type == pygame.KEYUP: #Клавиша отпущена
            print('Клавиша отпущена')
            if event.key == pygame.K_DOWN:
                down = False
            if event.key == pygame.K_UP:
                up = False
            if event.key == pygame.K_LEFT:
                left = False
            if event.key == pygame.K_RIGHT:
                right = False

    keys = pygame.key.get_pressed()#Получить кортеж нажатых клавиш

    #Управление на WASD
    if keys[pygame.K_a]:
        x -= speed
    if keys[pygame.K_d]:
        x += speed
    if keys[pygame.K_w]:
        y -= speed
    if keys[pygame.K_s]:
        y += speed
    if keys[pygame.K_ESCAPE]:
        # print(keys[pygame.K_ESCAPE])
        exit()

    #Перемещение с помощью стрелок
    if down:
        y += speed
    if up:
        y -= speed
    if left:
        x -= speed
    if right:
        x += speed

    pygame.draw.rect(screen, BLUE, (x, y, 50, 50),5)
    pygame.draw.rect(screen, BLUE, (x+10, y+10, 30, 30),5)

    pygame.display.update() # Обновление дисплея
    screen.fill(WHITE)
    clock.tick(FPS) #
