import pygame
from pygame.locals import *
import time


pygame.init() # Инициализация модуля pygame
pygame.display.set_caption("Game") # Создание заголовка игры
screen = pygame.display.set_mode((800,600)) # Создание поверхности игры
clock = pygame.time.Clock()

# Прямоугольник со сторонами 150*30 и координатами на 100,100
r1 = Rect(100,100,150,30)

r2 = Rect(300,400,180,100)


play = True

while play:
    for event in pygame.event.get(): # Проход по всем событиям
        if event.type == QUIT: # Если мы нажали на крестик
            play = False
    screen.fill((23, 93, 102))
    sky = pygame.draw.rect(screen,(101, 179, 252),(0,0,800,300))
    ground = pygame.draw.rect(screen,(35, 252, 82),(0,300,800,500))
    sun = pygame.draw.circle(screen,(232, 252, 8),(800,0),100)
    home = pygame.draw.rect(screen, (84, 48, 8), (250, 250, 200, 200))
    roof = pygame.draw.polygon(screen,(252, 33, 33),((250, 250),(450,250),(350,100)))

    pygame.draw.line(screen,(232, 252, 8),(800,0),(700,150),10)
    pygame.draw.line(screen, (232, 252, 8), (800, 0), (650, 100), 10)
    pygame.draw.line(screen, (232, 252, 8), (800, 0), (630, 50), 8)
    pygame.draw.line(screen, (232, 252, 8), (800, 0), (620, 10), 8)
    pygame.draw.line(screen, (232, 252, 8), (800, 0), (770, 170), 10)
    # pygame.draw.ellipse(screen,(255,50,108),r2,5)
    # pygame.draw.polygon(screen,(255,255,255),((200,300),(300, 100),(400,300)))
    pygame.display.update() # Обновить экран
    clock.tick(60) # Замедляем игру до 60 фпс