# -*- coding: utf-8 -*-
#Surface - поверхность, метод blit
#События мыши


import pygame
pygame.init()

W, H = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
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
speed = 10

StartDraw = False

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


    surf = pygame.Surface((200,200))
    surf.fill(YELLOW)
    pygame.draw.rect(surf,RED,(100,100,50,50))
    pygame.draw.polygon(surf,RED,((100,100),(125,60),(150,100)))

    # for x in range(800):
    #     for y in range(600):
    #         screen.blit(surf,(x,y))
    #         screen.blit(surf,(x+150,y))





    pygame.display.update() # Обновление дисплея
    screen.fill(BLACK)
            # clock.tick(FPS) #


