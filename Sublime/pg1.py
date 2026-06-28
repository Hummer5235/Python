import pygame
from pygame.locals import* # Импорт всех частей pygame.locals
#Класс - новый Тип данных, созданный пользователем

pygame.init() #Инициализация pygame
pygame.display.set_caption("First game") # Название окна
screen=pygame.display.set_mode((800,600)) #Размеры окна
 
r1=Rect(100,100,200,100)
r2=Rect(400,300,400,400)

#Отрисовка изображений (Графических примитивов)
#Отрисовка прямоугольников
pygame.draw.rect(screen,(0,255,0),(r1))
pygame.draw.rect(screen,(255,0,0),(r2))

#Отрисовка кругов
pygame.draw.circle(screen,(255,255,0),(400,300),200)

#Остальное
pygame.draw.polygon(screen,(30,140,200),((200,100),(400,100),(300,200)))
#Эллипс
pygame.draw.arc(screen,(255,0,0),r1,0,3.14,15)


#Программа отрисовки
play = True
clock = pygame.time.Clock()
while play:
	for event in pygame.event.get():
		if event.type == QUIT :
			play = false
	pygame.display.update() #Обновление 
	clock.tick(30)

