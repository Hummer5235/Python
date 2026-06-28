# Рисование объектов
# Отслеживание различных событий(клавитуры, мыши, таймера и т.д.)
# Отслеживание и изменение состояний объектов (анимация, столковение объектов)
# Быстрая отрисовка изменений на экране
# Работа со звуком

import pygame # Подгрузить библиотеку pygame
pygame.init() # Запуск pygame


#Каркас приложения
W,H = 600, 400

sc = pygame.display.set_mode((600,400)) # Создать окно размером 600 на 400
pygame.display.set_caption('Моя игра на Pygame') # Создать заголовок для окна
pygame.display.set_icon(pygame.image.load('images/rocket.png')) # Установить иконку



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


