import pygame
from pygame import * # Импортировать все переменные из pygame
import random


pygame.init()
pygame.display.set_caption('Snake')
W,H = 800, 600
screen = pygame.display.set_mode((W,H))

clock = pygame.time.Clock() # Создать часы 

#Цвета
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
YELLOW = (255,255,0)
RED = (255,0,0)
Brown = (94, 67, 47)

Play = True
Flag = True
GameOver = True


# pygame.mixer.music.load('Music/Music1_Deep.mp3')
# pygame.mixer.music.queue('Music/Music2_Deep.mp3')
# pygame.mixer.music.queue('Music/relaxed-vlog-night-street-131746.mp3')
# pygame.mixer.music.queue('Music/weeknds-122592.mp3')
# pygame.mixer.music.queue('Music/ambient-classical-guitar-144998.mp3')


pygame.mixer.music.load('Music/relaxed-vlog-night-street-131746.mp3')
# pygame.mixer.music.load('Music/weeknds-122592.mp3')

coin_sound = pygame.mixer.Sound('Music/coin.wav') # Звук монеты
death_sound = pygame.mixer.Sound('Music/death.wav')
# coin_sound.play() # Проиграть звук


pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)#Установить громкость


bg = pygame.image.load('images/Background2.jpg')
bg = pygame.transform.scale(bg,(800,600))
head = Rect(400,300,30,30) #Создать переменную head 

paused = True
SPEED = 20
DIRECTION = (SPEED,0)
GAME_POINTS = 0

def pickup(): # Функция сбора яблочка
	global GAME_POINTS,snake
	if head_rect.colliderect(apple_rect): # Проверка на столкновение прямоугольников
		GAME_POINTS += 1
		apple_rect.center = (random.randint(0,800),random.randint(0,600)) # Сменить координаты x,y на случайные
		snake.append(snake[-1].copy())
		coin_sound.play()  # Проиграть звук

		
def game_over():
	#Проверить каждый элемент списка snake на столкновение с головой
	global Flag, GameOver,Play

	if Flag :
		for i in snake[3:]:
			if head_rect.colliderect(i):
				Flag = False
				print('Game Over')
				death_sound.play()
	if Flag == False:
		pygame.mixer.music.stop()
		while GameOver:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					GameOver = False
					Play = False

			for element in snake[:0:-1]:
				screen.blit(body_image, element)
			screen.blit(head_image, head_rect)

			clock.tick(10)
			blit_text('Game Over')
			pygame.display.update()






def blit_text(text,x=0,y=0,font_size= 80,font_style='harlowsolid'):
	sys_font = pygame.font.SysFont(font_style, font_size)  # Выбираем шрифт
	screen_text = sys_font.render(f'{text}',1,BLACK)
	pos = screen_text.get_rect()
	pos.centerx = W//2+x
	pos.centery= H//2+y
	screen.blit(screen_text,pos)

def score():
	sys_font = pygame.font.SysFont('harlowsolid',50) #Выбираем шрифт
	screen_text = sys_font.render(f'Score:{GAME_POINTS}',1,RED) # Создаем поверхность с текстом
	pos = screen_text.get_rect()
	screen.blit(screen_text,pos)


def load_image(way, x, y):
	image = pygame.image.load(way) # Загрузить картинку
	image = pygame.transform.scale(image,(30,30)) # Изменить размер
	rect = image.get_rect() # Получить координаты и размер
	rect.center = (x,y) # Задать центр rect картинки
	return image, rect

def random_color():
	r = random.randint(0,255)
	g = random.randint(0,255)
	b = random.randint(0,255)
	return (r,g,b)

def move(head):
	global DIRECTION,COLOR
	
	if KEYS[K_w] and DIRECTION[1]==0:
		DIRECTION = (0,-SPEED)
	elif KEYS[K_s] and DIRECTION[1]==0:
		DIRECTION = (0,SPEED)
	elif KEYS[K_d] and DIRECTION[0]==0:
		DIRECTION = (SPEED,0)
	elif KEYS[K_a] and DIRECTION[0]==0:
		DIRECTION = (-SPEED,0)

	elif KEYS[K_SPACE]:
		DIRECTION = (0,0)
	
	if head.bottom > 600:
		head.top = 0
		COLOR = random_color()
	elif head.top < 0:
		head.bottom = 600
		COLOR = random_color()
	elif head.left < 0:
		head.right=800
		COLOR = random_color()
	elif head.right > 800:
		head.left=0
		COLOR = random_color()

	for index in range(len(snake)-1,0,-1):
		snake[index].x = snake[index-1].x
		snake[index].y = snake[index-1].y
		

	head.move_ip(DIRECTION)  # Метод для движения Rect



def pause():
	#Змейка не перемещается
	#Музыка на паузу
	#Звук нажатия на паузу
	#Рисование надписи "Пауза"
	Paused = True
	pygame.mixer.music.pause()
	global Play
	while Paused:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				Paused = False
				Play = False

		KEYS = pygame.key.get_pressed()
		if KEYS[K_RETURN] 	:
			pygame.mixer.music.unpause()
			Paused = False


		blit_text('Pause',y=-120,font_size = 70,font_style='Chiller')
		blit_text('Press "Enter" or "ESC"',y=80,font_size = 70,font_style='Chiller')

		pygame.display.update()  # Обновить дисплей`
		clock.tick(10)







#Загружаем картинки
head_image , head_rect = load_image('images/head.png',400,300)
body_image, body_rect = load_image('images/body.png',430,330)
apple_image, apple_rect = load_image('images/apple.png',200,300)


#Список в котором будут храниться координаты частей змейки
snake = [head_rect,body_rect] 



COLOR = random_color()
while Play:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			Play = False

	KEYS = pygame.key.get_pressed() #Получить список нажатых клавиш

	screen.fill(BLACK) #Команда залить экран
	screen.blit(bg,(0,0))
	screen.blit(apple_image,apple_rect) #Отрисовать на экране яблоко
	# screen.blit(body_image,body_rect) #Отрисовать на экране яблоко
	game_over()
	#Рисуем все части тела на координатах
	for element in snake[:0:-1]:
		screen.blit(body_image,element)
	screen.blit(head_image, head_rect)
	pickup()
	score()

	if KEYS[K_ESCAPE]:
		pause()

	move(head_rect) # Двигай голову

	pygame.display.update() #Обновить дисплей
	clock.tick(10) #Сделать задержку

pygame.quit()