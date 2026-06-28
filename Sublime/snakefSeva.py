import pygame
from pygame.locals import*
from sys import exit
from random import randint




#cd OneDrive\Документы\SublimeText


# pygame.mixer.init()
# gamesound = pygame.mixer.Sound("gamesound.wav")
# gamesound.set_volume(0.5)
# point = pygame.mixer.Sound("point.wav")
# point.set_volume(0.5)

pygame.init()
pygame.display.set_caption("Snake")
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()


SPEED = 30
# head = Rect(400,300,30,30)
COLOR = (255,255,255) 
gamepoint = 0
DIRECTION = [SPEED,0]
# bg_image = pygame.image.load("fon2.png")
# bg_image = pygame.transform.scale(bg_image,(800,600))
font = pygame.font.SysFont(None,32)


def load_image(src,x,y,x2,y2):
	image = pygame.image.load(src).convert() # Подключаем изображение к игре
	image = pygame.transform.scale(image,(x2,y2)) # Изменить размер 
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
		



	for index in range(len(snake)-1,0,-1):
		snake[index].x = snake[index-1].x
		snake[index].y= snake[index-1].y



	head.move_ip(DIRECTION) # Задать движение объекта Rect

def pickup():
	global apple_rect,head_rect,gamepoint,snake
	if head_rect.colliderect(apple_rect):
		apple_rect.x = randint(40,760)
		apple_rect.y = randint(40,560)
		gamepoint+=10
		print(f"GAME_POINTS: {gamepoint}")
		snake.append(snake[-1].copy())
		# point.play()



def gameover():
	global snake,head_rect
	for sig in snake[1:]:
		if head_rect.colliderect(sig):
			return True
	return False

# def ex(a):
# 	if a == False:
# 		pass
# 	else:
# 		exit()




def score():
	global gamepoint
	text = font.render(f"Score: {gamepoint}",True,(52, 207, 196))
	text_rect = text.get_rect(center = (700,50))
	screen.blit(text,text_rect)


head_image, head_rect = load_image("head.png",400,300,30,30)
apple_image, apple_rect = load_image("apple.png",200,300,40,40)
body_image, body_rect = load_image("body.png",370,300,30,30)

snake = [head_rect,body_rect]

while 1:
	# gamesound.play()
	screen.fill((0,0,0)) # Заполнить экран черным цветом
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			exit() 

	# print(head_rect)
	# pygame.draw.rect(screen,COLOR,head)

	# screen.blit(bg_image,(0,0))
	screen.blit(head_image,head_rect)
	screen.blit(apple_image,apple_rect)

	for segment in snake[1:]:
		screen.blit(body_image,segment)




	
	KEYS = pygame.key.get_pressed() # Получить все нажатые клавиши 

	pickup()
	score()
	move(head_rect,snake)
	if gameover():
		print("Jr")
		pygame.quit()
		exit()
	pygame.display.update()
	clock.tick(10)