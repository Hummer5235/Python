#Анимация кубиков

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
W,H = 800, 400

screen = pygame.display.set_mode((800,600)) # Создать окно размером 600 на 400
pygame.display.set_caption('Моя игра на Pygame') # Создать заголовок для окна
pygame.display.set_icon(pygame.image.load('images/rocket.png')) # Установить иконку






# В каждом приложении должен быть главный цикл обработки событий
Play = True

FPS = 100
сlock = pygame.time.Clock() #Создать объект класса Clock
x1 = 300
y1 = 300

while Play:
	for event in pygame.event.get():  # Перебираем очередь событий
		if event.type == pygame.QUIT: # Если тип события равен "выход", то
			Play = False
	screen.fill(BLACK)

	pygame.draw.rect(screen,GREEN,(x1,y1,50,50))

	
	if x1 < W:
		x1 += 3
	else:
		x1 = -50

	



	pygame.display.update() # Обновить дисплей
	сlock.tick(FPS)


pygame.quit() # Выйти из pygame
print('Программа закончилась')


