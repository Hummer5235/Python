import pygame ,sys
from pygame.locals import*
from sys import exit
from random import randint


pygame.init()
pygame.display.set_caption("Snake")
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Consolas",30) # Подключение шрифта
font2 = pygame.font.SysFont("Consolas",100) # Подключение шрифта


pygame.mixer.init() # Загрузка модуля миксер

game_sound = pygame.mixer.music
game_sound.load("Space1.mp3")

# game_sound.set_volume(0.5)
point_sound = pygame.mixer.Sound("Point.wav")  # Звук сбора яблока
point_sound.set_volume(0.2)
game_sound.set_volume(0.5)

SPEED = 30
# head = Rect(400,300,30,30)
COLOR = (255,255,255) 
DIRECTION = [SPEED,0]
GAME_POINTS = 0

background = pygame.image.load("back.jpg")
background = pygame.transform.scale(background,(800,600))
bc_rect = background.get_rect()




def load_image(src,x,y):
	image = pygame.image.load(src).convert() # Подключаем изображение к игре
	image = pygame.transform.scale(image,(30,30)) # Изменить размер 
	rect = image.get_rect(center = (x,y)) # Возвращает объект Rect с координатами центра в перед. кортеже

	transparent = image.get_at((0,0)) # Получает цвет пикселя
	image.set_colorkey(transparent) # Делает переданный цвет изображения прозрачным 

	return image, rect


def random_color(): # Функция случайного цвета
	r = randint(0,255) 
	g = randint(0,255)
	b = randint(0,255)
	return r,g,b


def move(head,snake):
	global DIRECTION,KEYS,SPEED,COLOR

#Нажатие клавиш
	if KEYS[K_UP] and DIRECTION[1]==0:
		DIRECTION = [0,-SPEED]
	elif KEYS[K_DOWN] and DIRECTION[1]==0:
		DIRECTION = [0,SPEED]
	elif KEYS[K_RIGHT] and DIRECTION[0]==0:
		DIRECTION = [SPEED,0]
	elif KEYS[K_LEFT] and DIRECTION[0]==0:
		DIRECTION = [-SPEED,0]

# Касание стен
	if head.bottom > 600:
		head.top=0
	elif head.top < 0:
		head.bottom = 600
	elif head.right > 800:
		head.left = 0
	elif head.left < 0 :
		head.right = 800
		
	for index in range(len(snake)-1,0,-1): # Обновление позиции сегментов змейки
		snake[index].x = snake[index-1].x
		snake[index].y = snake[index-1].y


	head.move_ip(DIRECTION) # Задать движение объекта Rect

def pickup():
	global apple_rect,head_rect,GAME_POINTS, snake

	if head_rect.colliderect(apple_rect): # Проверка коллизии головы и яблока , метод colliderect
		apple_rect.x = randint(40,760) # Обновление координат яблока
		apple_rect.y = randint(40,560)
		GAME_POINTS += 10
		print(f"GAME_POINTS: {GAME_POINTS}")
		snake.append(snake[-1].copy()) # Добавить сегмент змейки
		point_sound.play() # Сыграть звук сбора яблока


def score():
	global GAME_POINTS
	text = font.render(f"Score: {GAME_POINTS}",True,(255,255,0))
	text_rect = text.get_rect(center=(400,500))
	screen.blit(text,text_rect)


def gameover(): # Проигрыш
	global snake , head_rect
	for segment in snake[1:]:
		if head_rect.colliderect(segment): # Если голова пересекается с сегментом тела
			return True
	return False


head_image, head_rect = load_image("head.png",400,300) 
apple_image, apple_rect = load_image("apple.png",200,300)
body_image , body_rect = load_image("body.png",370,300)

snake = [head_rect,body_rect] # Список с сегментами змейки

game_sound.play(-1) # Игровая музыка запустить

while 1:
	screen.fill((0,0,0)) # Заполнить экран черным цветом
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	# print(head_rect)
	# pygame.draw.rect(screen,COLOR,head)
	

	screen.blit(background,bc_rect)
	screen.blit(head_image,head_rect)
	screen.blit(apple_image,apple_rect)
	
	for segment in snake[1:]:
		screen.blit(body_image,segment)
	

	
	KEYS = pygame.key.get_pressed() # Получить все нажатые клавиши 
	pickup()
	move(head_rect,snake)
	score()
	if gameover():  
		text3 = font2.render(f"Game Over",True,(255,255,0))
		text3_rect = text3.get_rect(center=(400,300))
		screen.blit(text3,text3_rect)
		SPEED = 0
	pygame.display.update()
	clock.tick(10)
	