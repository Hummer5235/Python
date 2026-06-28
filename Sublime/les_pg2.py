import pygame
from pygame.locals import*
from sys import exit
from random import randint


pygame.init()
pygame.display.set_caption("Snake")
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
SPEED = 3
head = Rect(400,300,30,30)
COLOR = (255,255,255) 

DIRECTION = [SPEED,0]

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
		# SPEED+=1
		DIRECTION = [0,-SPEED]
		COLOR = random_color()
	elif head.top < 0:
		# SPEED+=1
		DIRECTION = [0,SPEED]
		COLOR = random_color()
	elif head.right > 800:
		# SPEED+=1
		DIRECTION = [-SPEED,0]
		COLOR = random_color()
	elif head.left < 0 :
		# SPEED+=1
		DIRECTION = [SPEED,0]
		COLOR = random_color()





	head.move_ip(DIRECTION) # Задать движение объекта Rect




while 1:
	# screen.fill((0,0,0)) # Заполнить экран черным цветом
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			exit() 
	pygame.draw.rect(screen,COLOR,head)
	
	KEYS = pygame.key.get_pressed() # Получить все нажатые клавиши 
	move(head)

	pygame.display.update()
	clock.tick(30)