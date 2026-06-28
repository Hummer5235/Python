# Рисование объектов
# Отслеживание различных событий(клавитуры, мыши)

#4 типа событий
#pygame.MOUSEBUTTONDOWN - нажатие кнопки мыши
#pygame.MOUSEBUTTONUP - отпускание кнопки мыши
#pygame.MOUSEMOTION - перемещение мышки
#pygame.MOUSEWHEEL - кручение колесика мыши

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



x = 300
y = 300

cube_color = GREEN
flag_color =True 

# В каждом приложении должен быть главный цикл обработки событий
Play = True

FPS = 1
сlock = pygame.time.Clock() #Создать объект класса Clock
x = 0
y = 0


while Play:
	for event in pygame.event.get():  # Перебираем очередь событий
		if event.type == pygame.QUIT: # Если тип события равен "выход", то
			Play = False
	
	surf = pygame.Surface((200,200))	# Создать доп поверхность
	surf.fill(RED) # Залить поверхность



	
	surf_alpha = pygame.Surface((200,100)) #Создать доп поверхность
	surf_alpha.set_alpha(100) #Установить прозрачность
	surf.blit(surf_alpha,(0,50)) # На поверх 2 нарис поверхность 3


	pygame.draw.rect(surf,BLUE,(x,y,20,20))# Отобразить поверхность
	screen.blit(surf,(50,50))
	#screen.fill(BLACK)
	pygame.display.update() # Обновить дисплей
	сlock.tick(FPS)


pygame.quit() # Выйти из pygame
print('Программа закончилась')


