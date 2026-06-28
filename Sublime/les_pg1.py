import pygame
from pygame.locals import*
# import time


pygame.init() # Инициализация модуля pygame

pygame.display.set_caption("pygame") # Создание заголовка игры

screen = pygame.display.set_mode((800,600)) # Создание поверхности игры

clock = pygame.time.Clock() # Создание объекта класса Clock()

#Квадрат со стороной 50 с координатой верхней левой точки (100,100)
r1 = Rect(100,50,600,500)
r2 = Rect(200,150,50,50)
r3 = Rect(550,150,50,50)
r4 = Rect(385,250,50,150)
r5 = Rect(210,160,30,30)
r6 = Rect(560,160,30,30)



#Отрисовка квадрата r1 на пов-ти screen с заливкой зеленым цветом
pygame.draw.rect(screen,(251, 255, 5),r1)
pygame.draw.rect(screen,(0,0,0),r2)
pygame.draw.rect(screen,(0,0,0),r3)
pygame.draw.rect(screen,(0,0,0),r4)
pygame.draw.rect(screen,(255,255,255),r5)
pygame.draw.rect(screen,(255,255,255),r6)

#Отрисовка круга
pygame.draw.circle(screen,(255,0,0),(600,350),70)
pygame.draw.circle(screen,(255,0,0),(200,350),70)

#Отрисовка полигона. В кортеж передаются координаты точек
# pygame.draw.polygon(screen,(0,0,255),((100,50),(400,0),(700,50))

play = True

while play:
	for event in pygame.event.get(): # Цикл по всем событиям в игре
		if event.type == QUIT: #  Если мы нажали крестик, окно закроется
			play = False

	pygame.display.update()
	clock.tick(60) # Замедляем игру до 60 fps