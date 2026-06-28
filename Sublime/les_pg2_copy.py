import pygame
from pygame.locals import*
from sys import exit

pygame.init()
pygame.display.set_caption("Snake")
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
SPEED = 3
head = Rect(400,300,30,30)


DIRECTION = [SPEED,0]

def move(head):
	global DIRECTION,KEYS,SPEED

	if KEYS[K_UP]:
		DIRECTION = [0,-SPEED]
	elif KEYS[K_DOWN]:
		DIRECTION = [0,SPEED]
	elif KEYS[K_RIGHT]:
		DIRECTION = [SPEED,0]
	elif KEYS[K_LEFT]:
		DIRECTION = [-SPEED,0]



	if head.bottom > 600:
		DIRECTION = [0,-SPEED]
	elif head.top < 0:
		DIRECTION = [0,SPEED]
	elif head.right > 800:
		DIRECTION = [-SPEED,0]
	elif head.left < 0 :
		DIRECTION = [SPEED,0]






	head.move_ip(DIRECTION) # Задать движение объекта Rect




while 1:
	screen.fill((0,0,0)) # Заполнить экран черным цветом
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			exit() 
	pygame.draw.circle(screen,(255,0,0),(600,350),70)
	pygame.draw.rect(screen,(255,255,255),head)
	
	KEYS = pygame.key.get_pressed() # Получить все нажатые клавиши 
	move(head)

	pygame.display.update()
	clock.tick(30)