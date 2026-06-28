import pygame
from pygame.locals import* # Импорт всех частей pygame.locals
#Класс - новый Тип данных, созданный пользователем

pygame.init() #Инициализация pygame
pygame.display.set_caption("First game") # Название окна
screen=pygame.display.set_mode((800,600)) #Размеры окна
 
r1=Rect(300,100,200,100)
r2=Rect(200,200,400,100)
r3=Rect(100,300,600,100)
r4=Rect(350,400,100,200)



#Отрисовка изображений (Графических примитивов)
#Отрисовка прямоугольников
pygame.draw.rect(screen,(0,255,0),(r1))
pygame.draw.rect(screen,(0,255,0),(r2))
pygame.draw.rect(screen,(0,255,0),(r3))
pygame.draw.rect(screen,(40,120,79),(r4))



#Программа отрисовки
play = True
clock = pygame.time.Clock()
while play:
	for event in pygame.event.get():
		if event.type == QUIT :
			play = false
	pygame.display.update() #Обновление 
	clock.tick(30)

