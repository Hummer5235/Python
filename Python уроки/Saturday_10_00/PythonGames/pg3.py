# Рисование объектов
# Отслеживание различных событий(клавитуры)

#pygame.KEYDOWN: #Клавиша нажата
#pygame.KEYUP: #Клавиша отпущена

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

FPS = 200
сlock = pygame.time.Clock() #Создать объект класса Clock

speed = 1
flLeft = flRight = flUp = flDown = False




i = 1
while Play:
	for event in pygame.event.get():  # Перебираем очередь событий
		if event.type == pygame.QUIT: # Если тип события равен "выход", то
			Play = False
		elif event.type == pygame.KEYDOWN: #Клавиша нажата
			# print(f'Клавиша нажата {i} раз')
			i += 1
			if event.key == pygame.K_LEFT or event.key == pygame.K_a: #Клавиша влево
				# print('Стрелка влево')
				flLeft = True
			elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
				# print('Стрелка вправо')
				flRight = True
			elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
				# print('Стрелка вправо')
				flDown = True
			elif event.key == pygame.K_UP or event.key == pygame.K_w:
				# print('Стрелка вправо')
				flUp = True

			elif event.key == pygame.K_t:
				if flag_color == True:
					cube_color = WHITE
					flag_color = False
				else :
					cube_color = GREEN
					flag_color = True
				

		elif event.type == pygame.KEYUP:
			print('Клавиша отпущена')
			if event.key == pygame.K_LEFT or event.key == pygame.K_a:
				flLeft = False
			elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
				flRight = False
			elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
				flDown = False
			elif event.key == pygame.K_UP or event.key == pygame.K_w:
				flUp = False




	if flLeft :
		x -= speed
	if flRight:
		x += speed
	if flDown :
		y += speed
	if flUp:
		y -= speed


	#screen.fill(BLACK)
	pygame.draw.rect(screen,(color),(x,y,50,50))
	pygame.display.update() # Обновить дисплей
	сlock.tick(FPS)


pygame.quit() # Выйти из pygame
print('Программа закончилась')


