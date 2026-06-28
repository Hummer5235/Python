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
# Координаты начальной и конечной точки
sp = ep = None

sc.fill(WHITE)
pygame.display.update()



while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
		# elif event.type == pygame.MOUSEBUTTONDOWN:
		# 	print("Нажата кнопка",event.button)
		# elif event.type == pygame.MOUSEMOTION:
		# 	print("Позиция мыши",event.pos) event.rel #относительное положение мыши
		elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
			flStartDraw = True
			sp = event.pos
		elif event.type == pygame.MOUSEMOTION: # События движение мыши
			if flStartDraw:
				pos = event.pos

				width = pos[0] - sp[0]
				height = pos[1] - sp[1]


				sc.fill(WHITE)
				pygame.draw.rect(sc,RED,(sp[0],sp[1],width,height))
				pygame.display.update()

		elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
			flStartDraw = False



	clock.tick(FPS)
