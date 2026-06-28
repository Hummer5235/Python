import pygame
from pygame.locals import*
from sys import exit
from random import randint


pygame.init()
pygame.display.set_caption("Snake")
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()


SPEED = 3
# head = Rect(400,300,30,30)
COLOR = (255,255,255) 

DIRECTION = [SPEED,0]



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


def move(head):
	global DIRECTION,KEYS,SPEED,COLOR

#Нажатие клавиш
	if KEYS[K_UP]:
		DIRECTION = [0,-SPEED]
	elif KEYS[K_DOWN]:
		DIRECTION = [0,SPEED]
	elif KEYS[K_RIGHT]:
		DIRECTION = [SPEED,0]
	elif KEYS[K_LEFT]:
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
		
	head.move_ip(DIRECTION) # Задать движение объекта Rect




head_image, head_rect = load_image("head.png",400,300)
apple_image, apple_rect = load_image("apple.png",200,300)


while 1:
	screen.fill((0,0,0)) # Заполнить экран черным цветом
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			exit() 
	# print(head_rect)
	# pygame.draw.rect(screen,COLOR,head)

	screen.blit(head_image,head_rect)
	screen.blit(apple_image,apple_rect)
	

	
	KEYS = pygame.key.get_pressed() # Получить все нажатые клавиши 
	move(head_rect)
	
	pygame.display.update()
	clock.tick(30)