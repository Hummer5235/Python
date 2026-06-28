# Урок 3
#3.2: Создание класса кактусов.
import pygame
import random

pygame.init()

#Размеры экрана
display_width = 800
display_height = 600
display = pygame.display.set_mode((display_width,display_height)) # Установить размеры экрана
pygame.display.set_caption("Run Dino! Run!") # Установить название

icon = pygame.image.load("app_icon.png") # Загрузить изображение
pygame.display.set_icon(icon) # Установить иконку


class Cactus:
    def __init__(self,x,y,width,height,speed):
        self.x = x
        self.y = y
        self.width = width # Ширина
        self.height = height # Высота
        self.speed = speed # Скорость

    def move(self):
        if self.x >= - self.width:
            pygame.draw.rect(display, (230, 230, 0), (self.x, self.y, self.width, self.height))
            self.x -= self.speed  # Сместить кактус влево

        else:
            self.x = display_width + 100 + random.randint(-80,80)


#Персонаж
usr_width = 60   # Ширина персонажа
usr_height = 100 # Высота персонажа
usr_x = display_width //3 # Координата X героя
usr_y = display_height -100 - usr_height

#Кактус
cactus_width = 20  # Ширина кактуса
cactus_height = 70 # Высота кактуса
cactus_x = display_width - 50 # Координата X кактуса
cactus_y = display_height - 100 - cactus_height # Координата Y кактуса


#FPS
clock = pygame.time.Clock()

#Прыжок
make_jump = False
jump_counter = 30 # Счетчик прыжков




def run_game():
    global make_jump
    game = True
    cactus_arr = [] # Пустой список для кактусов
    create_cactus_arr(cactus_arr) # Заполнить список кактусов


    while game:
        for event in pygame.event.get(): # Пройтись по всем событиям
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed() # Получить кортеж нажатых клавиш
        if keys[pygame.K_SPACE]: # Если нажата клавиша пробел
            make_jump = True   # Разрешить прыжок

        if make_jump:
            jump()


        display.fill((255,255,255))
        draw_array(cactus_arr) # Отрисовать список
        pygame.draw.rect(display,(247,240,22),(usr_x,usr_y,usr_width,usr_height))
        pygame.display.update() # Обновить дисплей
        clock.tick(60)

def jump():
    global  usr_y,jump_counter ,make_jump
    if jump_counter >= -30:
        usr_y -= jump_counter / 2 # Поднимаем вверх на jump_counter
        jump_counter -= 1 # Уменьшаем jump_counter ( Замедляем прыжок)
    else:
        # Как только опустились на землю (jump_counter >= -30) вернуть все значения вначало
        jump_counter = 30
        make_jump = False
    print(jump_counter)

#Создать массив кактусов
def create_cactus_arr(array):
    array.append(Cactus(display_width + 50 ,display_height - 170,20,70,4))
    array.append(Cactus(display_width + 300 ,display_height - 150,30,50,4))
    array.append(Cactus(display_width + 600 ,display_height - 190,25,90,4))


#Отрисовать список
def draw_array(array):
    for cactus in array:
        cactus.move()

run_game()


















