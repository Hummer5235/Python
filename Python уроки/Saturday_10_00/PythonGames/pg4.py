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

FPS = 2000
сlock = pygame.time.Clock() #Создать объект класса Clock

speed = 1
flLeft = flRight = flUp = flDown = False

start_draw = False # Флаг для проверки, рисовать или нет
start_draw_rect = False
start_pos = 0


while Play:
	for event in pygame.event.get():  # Перебираем очередь событий
		if event.type == pygame.QUIT: # Если тип события равен "выход", то
			Play = False
		
		elif event.type == pygame.MOUSEBUTTONDOWN:
			print('Нажата кнопка',event.button,event.pos)
			if event.button == 1: #Нажата левая кнопка мыши
				start_draw = True
				pygame.draw.rect(screen,WHITE,(500,500,-50,-50))	


			elif event.button == 3: #Нажата правая кнопка мыши
				start_pos = event.pos
				start_draw_rect = True



		elif event.type == pygame.MOUSEBUTTONUP:
			if event.button == 1: #Отпущена левая кнопка мыши
				start_draw = False
			elif event.button == 3: #Нажата правая кнопка мыши
				start_draw_rect = False


		elif event.type == pygame.MOUSEMOTION:
			# print('Движется',event.pos)
			if start_draw == True:
				pygame.draw.rect(screen,WHITE,(event.pos[0],event.pos[1],10,10))

			if start_draw_rect == True:
				#Вычисляем размеры прямоугольника
				screen.fill(BLACK)
				width = event.pos[0]-start_pos[0]
				height = event.pos[1]-start_pos[1]


				pygame.draw.rect(screen,WHITE,(start_pos[0],start_pos[1],width,height))	





	screen.fill(BLACK)
	pygame.draw.rect(screen,(cube_color),(x,y,50,50))
	x += 0.01
	pygame.display.update() # Обновить дисплей
	сlock.tick(FPS)


pygame.quit() # Выйти из pygame
print('Программа закончилась')



#Функции для рисования
#pygame.draw.rect(surface,...) - прямоугольник
#pygame.draw.line(surface,...) - линия
#pygame.draw.polygon(surface,...) - полигон
#pygame.draw.circle(surface,...) - круг