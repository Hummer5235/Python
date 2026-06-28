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



screen = pygame.display.set_mode((W,H)) # Создание окна
pygame.display.set_caption('Мое окно')
pygame.display.set_icon(pygame.image.load('Icon1.png'))



clock = pygame.time.Clock() # создай экз часы
FPS = 20


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.draw.rect(screen,RED,(10,10,500,500),3) #Рисование прямоугольника
    pygame.draw.rect(screen,GREEN,(20,20,480,480),3)
    pygame.draw.rect(screen,BLUE,(30,30,460,460),3)
    pygame.draw.polygon(screen,BLUE,((250,100),(200,200),(600,200)))
    pygame.draw.line(screen,YELLOW,(30,30),(490,490),5)
    # pygame.draw.line()

    pygame.display.update() # Обновление дисплея
    clock.tick(FPS) #

