#Создание поверхностей(Surface), анимация, метод blit


# Рисование объектов


import pygame # Подгрузить библиотеку pygame
pygame.init() # Запуск pygame


#Цвета
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)
Brown = (94, 67, 47)

#Каркас приложения
W,H = 800, 400

screen = pygame.display.set_mode((800,600)) # Создать окно размером 600 на 400
pygame.display.set_caption('Класс Surface') # Создать заголовок для окна
pygame.display.set_icon(pygame.image.load('images/rocket.png')) # Установить иконку



screen.fill((0, 0, 0))

# #Создать доп поверхность
# surf = pygame.Surface((200,200))
# surf.fill(RED) # Заливаем поверхность
# for i in range(10):
# 	pygame.draw.rect(surf,(22, 155, 250),(20*i,20*i,20,20))


# #Создать доп поверхность
# surf_alpha = pygame.Surface((200,100)) 
# pygame.draw.rect(surf_alpha,BLUE,(0,0,200,100))
# surf_alpha.set_alpha(100) #Установить прозрачность



# #На поверх 2 нарис поверхность 3
# surf.blit(surf_alpha,(0,50))
# #На экране нарис поверхность 2
# screen.blit(surf,(250,200))

surf = pygame.Surface((W,200))
second_surf = pygame.Surface((50,10))

surf.fill(BLUE)
second_surf.fill(RED) 

sec_s_x, sec_s_y = 0, 150
x, y = 0 ,0 




# В каждом приложении должен быть главный цикл обработки событий
Play = True

FPS = 60
сlock = pygame.time.Clock() #Создать объект класса Clock

while Play:
	for event in pygame.event.get():  # Перебираем очередь событий
		if event.type == pygame.QUIT: # Если тип события равен "выход", то
			Play = False
			
	surf.fill(BLUE)
	surf.blit(second_surf,(sec_s_x,sec_s_y))

	if sec_s_x < W:
		sec_s_x += 5
	else:
		 sec_s_x = 0

	if y < H:
		y+=1
	else:
		y = 0


	screen.fill(WHITE)
	screen.blit(surf,(x,y))
	pygame.display.update() # Обновить дисплей
	сlock.tick(FPS)


pygame.quit() # Выйти из pygame
print('Программа закончилась')

