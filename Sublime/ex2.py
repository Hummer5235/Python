# pygame события с мышкой

import pygame

pygame.init()

W = 600
H = 400


sc = pygame.display.set_mode((W,H))
pygame.display.set_caption("События от мыши")
pygame.display.set_icon(pygame.image.load("head.png"))

WHITE = (255,255,255)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)

FPS = 60
clock = pygame.time.Clock()

#	Флаг, что рисуем прямоугольник
flStartDraw = False 

sp = None # Начальная точка

sc.fill(WHITE)
pygame.display.update()



while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
		
		pressed = pygame.mouse.get_pressed()
		if pressed[0]: # Левая кнопка [0] , средняя [1], правая [2]
			pos = pygame.mouse.get_pos()

			if sp is None:
				sp = pos
			width = pos[0]-sp[0] 
			height = pos[1]-sp[1] 

			sc.fill(WHITE)
			pygame.draw.rect(sc,RED,(sp[0],sp[1],width,height))
			pygame.display.update()

		else:
			sp = None

	clock.tick(FPS)
