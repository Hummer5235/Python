# Урок 3
#3.1: Образ объектов, анимация движения, преграды
import pygame

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
            self.x = display_width - 50  # Восстановить значение по умолчанию


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
        draw_cactus() # Нарисовать кактусы
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


def draw_cactus():
    global cactus_x , cactus_y , cactus_width , cactus_height

    if cactus_x >= - cactus_width:
        pygame.draw.rect(display,(230,230,0),(cactus_x,cactus_y,cactus_width,cactus_height))
        cactus_x -=4 # Сместить кактус влево

    else:
        cactus_x = display_width - 50 # Восстановить значение по умолчанию

run_game()


















