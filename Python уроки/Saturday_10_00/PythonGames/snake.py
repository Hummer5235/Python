import pygame
from pygame import * # Импортировать все переменные из pygame
import random

pygame.init()
pygame.display.set_caption('Snake')
screen = pygame.display.set_mode((800,600))

clock = pygame.time.Clock() # Создать часы 

#Цвета
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
YELLOW = (255,255,0)
RED = (255,0,0)
Brown = (94, 67, 47)




head = Rect(400,300,30,30) #Создать переменную head 

SPEED = 2
DIRECTION = (SPEED,0)


def random_color():
	r = random.randint(0,255)
	g = random.randint(0,255)
	b = random.randint(0,255)
	return (r,g,b)

def move(head):
	global DIRECTION,COLOR
	
	if KEYS[K_w]:
		DIRECTION = (0,-SPEED)
	elif KEYS[K_s]:
		DIRECTION = (0,SPEED)
	elif KEYS[K_d]:
		DIRECTION = (SPEED,0)
	elif KEYS[K_a]:
		DIRECTION = (-SPEED,0)

	elif KEYS[K_SPACE]:
		DIRECTION = (0,0)

	if head.bottom > 600:
		DIRECTION = (0,-SPEED)
		COLOR = random_color()
		
	elif head.top < 0:
		DIRECTION = (0,SPEED)
		COLOR = random_color()
	elif head.left < 0:
		DIRECTION = (SPEED,0)
		COLOR = random_color()
	elif head.right > 800:
		DIRECTION = (-SPEED,0)
		COLOR = random_color()

	head.move_ip(DIRECTION)  # Метод для движения Rect

Play = True

COLOR = random_color()
while Play:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			Play = False

	KEYS = pygame.key.get_pressed() #Получить список нажатых клавиш

	#screen.fill(BLACK) #Команда залить экран
	pygame.draw.rect(screen,COLOR,head)
	move(head) # Двигай голову

	pygame.display.update() #Обновить дисплей
	clock.tick(60) #Сделать задержку

pygame.quit()