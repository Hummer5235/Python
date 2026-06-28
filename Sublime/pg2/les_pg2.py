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
		SPEED=SPEED+10
		DIRECTION = [0,-SPEED]
		
	elif head.top < 0:
		SPEED=SPEED+10
		DIRECTION = [0,SPEED]
		
	elif head.right > 800:
		SPEED=SPEED+10
		DIRECTION = [-SPEED,0]

	elif head.left < 0 :
		SPEED=SPEED+10

		DIRECTION = [SPEED,0]
	SPEED=SPEED+10







	head.move_ip(DIRECTION) # Задать движение объекта Rect




while 1:
	screen.fill((0,0,0)) # Заполнить экран черным цветом
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			exit() 
	pygame.draw.rect(screen,(255,255,255),head)
	
	KEYS = pygame.key.get_pressed() # Получить все нажатые клавиши 
	move(head)

	pygame.display.update()
	clock.tick(30)