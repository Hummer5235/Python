import pygame
from pygame.locals import*
from sys import exit

pygame.init()
pygame.display.set_caption("Snake")
screen=pygame.display.set_mode((800,600))
clock= pygame.time.Clock()

head=Rect(400,300,30,30)

DIRECTION= [2,0]
SPEED = 10
def move(head): 
	global DIRECTION,KEYS,SPEED
	if KEYS[K_UP]:
		DIRECTION = [0,-SPEED]
	elif KEYS[K_DOWN]:
		DIRECTION = [0,SPEED]
	elif KEYS[K_LEFT]:
		DIRECTION = [-SPEED,0]
	elif KEYS[K_RIGHT]:
		DIRECTION = [SPEED,0]


	if head.bottom > 600:
		DIRECTION = [0,-SPEED ]
	elif head.top < 0:
		DIRECTION=[0,SPEED]
	elif head.left < 0:
		DIRECTION = [SPEED,0]
	elif head.right > 800:
		DIRECTION = [-SPEED,0]

	head.move_ip(DIRECTION)


while 1:
	screen.fill((0,0,0))
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			exit()
	pygame.draw.rect(screen,(255,255,255),head)
	KEYS = pygame.key.get_pressed()
	move(head)
	

	pygame.display.update()
	clock.tick(30)