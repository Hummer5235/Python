import pygame
from pygame.locals import*
import time

pygame.init() # Запуск модуля pygame
pygame.display.set_caption("PG") #Содание заголовка игры
screen = pygame.display.set_mode((1000,800)) # Создание поверхности игры


r1 = Rect(100,50,600,500)
r2 = Rect(200,150,50,50)
r3 = Rect(550,140,50,50)
r4 = Rect(350,300,50,150)
clock = pygame.time.Clock()

pygame.draw.rect(screen,(251, 255, 5),r1)
pygame.draw.rect(screen,(0, 0, 0),r2)
pygame.draw.rect(screen,(0, 0, 0),r3)
pygame.draw.rect(screen,(0, 0, 0),r4)

play = True
while play:
	for event in pygame.event.get(): # Цикл по всем событиям в игре
		if event.type == QUIT: # Если мы нажали крестик, окно закроется
			play = False

	pygame.display.update()
	clock.tick(60)		