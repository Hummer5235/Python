# Урок 5
#5.1: Элементы реалистичности
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

land_img = pygame.image.load("Pygame materials/Backgrounds/Land.jpg") # Фон

cactus_img = [pygame.image.load("Pygame materials/Objects/Cactus0.png"),
              pygame.image.load("Pygame materials/Objects/Cactus1.png"),
              pygame.image.load("Pygame materials/Objects/Cactus2.png")]

cactus_options = [69,449,37,410,40,420] # Параметры кактусов

stone_img = [pygame.image.load("Pygame materials/Objects/Stone0.png"),
             pygame.image.load("Pygame materials/Objects/Stone1.png")]  # Список Камней

cloud_img = [pygame.image.load("Pygame materials/Objects/Cloud0.png"),
             pygame.image.load("Pygame materials/Objects/Cloud1.png")]  # Список Облаков

print(cactus_options)


class Object:
    def __init__(self,x,y,width,image,speed):
        self.x = x
        self.y = y
        self.width = width # Ширина
        self.image = image # Картинка
        self.speed = speed # Скорость

    def move(self):
        if self.x >= - self.width:
            display.blit(self.image,(self.x,self.y))
            # pygame.draw.rect(display, (230, 230, 0), (self.x, self.y, self.width, self.height))
            self.x -= self.speed  # Сместить кактус влево
            return True

        else:
            #self.x = display_width + 100 + random.randint(-80,80)
            return False

    def return_self(self,radius, y, width, image):
        self.x = radius
        self.y = y
        self.width = width
        self.image = image

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
    land = Object(0, 0, 800, land_img, 4) # Создание фона как объекта класса Object
    land2 = Object(display_width, 0, 800, land_img, 4) # Создание фона2 как объекта класса Object
    stone,cloud = open_random_objects() # Создать случайный объект


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


        # display.blit(land,(0,0)) # Отрисовать картинку
        move_objects(stone,cloud,land,land2) # Двигать камни и облака
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
    choice = random.randrange(0,3) # Выбор
    img = cactus_img[choice]
    width = cactus_options[choice * 2]
    height = cactus_options[choice * 2 + 1 ]
    array.append(Object(display_width + 50, height, width, img, 4))

    choice = random.randrange(0, 3)  # Выбор
    img = cactus_img[choice]
    width = cactus_options[choice * 2]
    height = cactus_options[choice * 2 + 1]
    array.append(Object(display_width + 300, height, width, img, 4))

    choice = random.randrange(0, 3)  # Выбор
    img = cactus_img[choice]
    width = cactus_options[choice * 2]
    height = cactus_options[choice * 2 + 1]
    array.append(Object(display_width + 600, height, width, img, 4))



def find_radius(array):
    maximum = max(array[0].x,array[1].x,array[2].x)

    if maximum < display_width:
        radius = display_width
        if radius - maximum < 50:
            radius += 150
    else:
        radius = maximum

    choice = random.randrange(0,5) # Переменная случайного выбора
    if choice == 0:
        radius += random.randrange(10,15)
    else:
        radius += random.randrange(200,350)

    return radius


#Отрисовать список
def draw_array(array):
    for cactus in array:
        check = cactus.move()
        if not check:
            radius = find_radius(array) #  Найти радиус

            choice = random.randrange(0, 3)  # Выбор
            img = cactus_img[choice]
            width = cactus_options[choice * 2]
            height = cactus_options[choice * 2 + 1]

            cactus.return_self(radius, height, width, img) # Вернуть себя
def open_random_objects():
    choice = random.randrange(0,2)
    img_of_stone= stone_img[choice]

    choice = random.randrange(0, 2)
    img_of_cloud = cloud_img[choice]

    stone = Object(display_width,display_height-80,10,img_of_stone,4)
    cloud = Object(display_width,80,70,img_of_cloud,2)

    return stone,cloud

def move_objects(stone,cloud,land,land2):
    check = land.move()
    if not check:
        land.return_self(display_width, 0, land.width, land_img)

    check = land2.move()
    if not check:
        land2.return_self(display_width, 0, land2.width, land_img)

    check = stone.move()
    if not check:
        choice = random.randrange(0,2)
        img_of_stone = stone_img[choice]
        stone.return_self(display_width,500 + random.randrange(10,80),stone.width,img_of_stone)

    check = cloud.move()
    if not check:
        choice = random.randrange(0, 2)
        img_of_cloud = cloud_img[choice]
        cloud.return_self(display_width, random.randrange(10, 200), cloud.width, img_of_cloud)



run_game()





















