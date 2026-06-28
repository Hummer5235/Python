#Рисование текста различными шрифтами

'''
pygame.font - модуль со шрифтами

SysFont(fontname,size) - класс для выбора системного шрифта fontname, по размеру size.  SysFont('Arial',12)

'''

import pygame
pygame.init()

# print(pygame.font.get_fonts()) # Получить список шрифтов

#Цвета
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)


sys_font = pygame.font.SysFont('Consolas',30) #Выбираем шрифт
screen_text = sys_font.render('Привет Мир!',1,RED) # Создаем поверхность с текстом
screen_text2 = sys_font.render('Привет Соня!',1,BLUE)
screen_text3 = sys_font.render('Привет Антон!',1,BLUE)
screen_text4 = sys_font.render('Привет Андрей!',1,BLUE)
screen_text5 = sys_font.render('Python is unbelievable',1,GREEN)
pos = screen_text.get_rect()
pos.center = 200,200



#Каркас приложения
W,H = 600, 400

screen = pygame.display.set_mode((600,400)) 

Play = True

FPS = 60
сlock = pygame.time.Clock() #Создать объект класса Clock


while Play:
	for event in pygame.event.get():  
		if event.type == pygame.QUIT: 
			Play = False
	screen.fill(BLACK)
	screen.blit(screen_text,pos)
	screen.blit(screen_text2,(300,250))
	screen.blit(screen_text3,(150,100))
	screen.blit(screen_text4,(150,200))
	screen.blit(screen_text5,(150,300))
	сlock.tick(FPS)
	pygame.display.update()
	

pygame.quit() 

