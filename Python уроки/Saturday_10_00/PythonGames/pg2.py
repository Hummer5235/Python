# Рисование объектов


import pygame # Подгрузить библиотеку pygame
pygame.init() # Запуск pygame


#Цвета
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)
Brown = (94, 67, 47)

#Каркас приложения
W,H = 600, 400

screen = pygame.display.set_mode((800,600)) # Создать окно размером 600 на 400
pygame.display.set_caption('Моя игра на Pygame') # Создать заголовок для окна
pygame.display.set_icon(pygame.image.load('images/rocket.png')) # Установить иконку



screen.fill((8, 163, 13))
pygame.draw.rect(screen,(22, 155, 250),(0,0,800,300))# Небо
pygame.draw.rect(screen,(222, 219, 133),(300,250,170,170))# Стены
pygame.draw.rect(screen,(38, 27, 19),(300,250,170,170),10)# Обводка
pygame.draw.rect(screen,(226, 255, 110),(350,300,70,70))# Окно
pygame.draw.rect(screen,(38, 27, 19),(350,300,70,70),10)# Окно

pygame.draw.polygon(screen,(122, 60, 42),[(250,260),(385,150),(510,260)])# Крыша
pygame.draw.polygon(screen,(38, 27, 19),[(250,260),(385,150),(510,260)],10)# Крыша
pygame.draw.circle(screen,(255,255,0),(800,0),80)# Солнце
pygame.draw.line(screen,(255,255,0),(710,10),(620,50),10)
# pygame.draw.line(screen,(255,255,0),(715,30),(620,90),10)
pygame.draw.line(screen,(255,255,0),(720,60),(610,130),10)
pygame.draw.line(screen,(255,255,0),(770,90),(660,190),10)




pygame.display.update() # Обновить дисплей

# В каждом приложении должен быть главный цикл обработки событий
Play = True

FPS = 60
сlock = pygame.time.Clock() #Создать объект класса Clock

while Play:
	for event in pygame.event.get():  # Перебираем очередь событий
		if event.type == pygame.QUIT: # Если тип события равен "выход", то
			Play = False

	сlock.tick(FPS)


pygame.quit() # Выйти из pygame
print('Программа закончилась')

