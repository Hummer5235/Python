# Рисование объектов
# Отслеживание различных событий(клавитуры, мыши, таймера и т.д.)
# Отслеживание и изменение состояний объектов (анимация, столковение объектов)
# Быстрая отрисовка изменений на экране
# Работа со звуком

import pygame # Подгрузить библиотеку pygame
pygame.init() # Запуск pygame


#Цвета
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)


#Каркас приложения
W,H = 600, 400

screen = pygame.display.set_mode((600,400)) # Создать окно размером 600 на 400
pygame.display.set_caption('Моя игра на Pygame') # Создать заголовок для окна
pygame.display.set_icon(pygame.image.load('images/rocket.png')) # Установить иконку


#Залить экран
screen.fill((255,255,255))


pygame.draw.rect(screen,BLUE,(10,10,50,100))
pygame.draw.rect(screen,WHITE,(60,10,50,100))
pygame.draw.rect(screen,RED,(110,10,50,100))

pygame.draw.line(screen,GREEN,(200,20),(350,50),10)
pygame.draw.line(screen,GREEN,(200,20),(350,50),10)

pygame.draw.lines(screen,RED,False,[(200,80),(250,80),(300,200),(150,200)],5)
pygame.draw.polygon(screen,WHITE,[(150,210),(180,250),(90,290),(30,230)])

pygame.draw.circle(screen,BLUE,(300,300),60,5)
pygame.draw.circle(screen,(147, 80, 235),(300,300),40)

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



#Функции для рисования
#pygame.draw.rect(surface,...) - прямоугольник
#pygame.draw.line(surface,...) - линия
#pygame.draw.polygon(surface,...) - полигон
#pygame.draw.circle(surface,...) - круг