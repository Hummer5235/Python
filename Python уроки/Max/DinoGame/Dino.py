

import pygame
import random, time
from pygame.locals import *

pygame.init()

#Размеры экрана

W,H = 800 , 600
display = pygame.display.set_mode((W,H))
pygame.display.set_caption("Run Maxim!")
icon = pygame.image.load("app_icon.png")
pygame.display.set_icon(icon)

#Загрузка звуков
pygame.mixer.music.load('Materials/Sounds/background.mp3')


#Загрузка изображений
land_img = pygame.image.load("Materials/Backgrounds/Land2.jpg")

cloud_img = [pygame.image.load("Materials/Objects/Cloud0.png"),
             pygame.image.load("Materials/Objects/Cloud1.png")]

cactus_img = [pygame.image.load("Materials/Objects/Cactus0(2).png"),
              pygame.image.load("Materials/Objects/Cactus1(2).png"),
              pygame.image.load("Materials/Objects/Cactus2(2).png")]

dino_img = [pygame.image.load('Materials/Dino/DinoRun1.png'),
            pygame.image.load('Materials/Dino/DinoRun2.png'),
            ]
# image1= pygame.image.load('Materials/Dino/TestDino.png')
# image1 = pygame.transform.scale(image1,(80,80))
# dino_img = [image1,image1,image1,image1]
img_counter = 0
cactus_options = [69, 449, 36, 412, 40, 420 ]
bomb_image = pygame.image.load('Materials/Objects/bomb.png')
bomb_image = pygame.transform.scale(bomb_image,(70,60))
# bomb_rect = pygame.rect.Rect(250,200,150,150)
dino_rect = dino_img[0].get_rect()



#Цвета
BG = (0, 0, 0)

#Персонаж
usr_width = 60
usr_height = 100
usr_x = W // 3
usr_y = H - 100 - usr_height
print(usr_x,usr_y,usr_width,usr_height)

#Кактус
cactus_width = 20
cactus_height = 70
cactus_x = W - 50
cactus_y = H - 100 - cactus_height


clock = pygame.time.Clock()

#Прыжок
make_jump = False
jump_counter = 30 # Счетчик прыжков
score = 0
max_score = 0 # Максимальные очки
cactuses_counter = []  # Список для катусов


class Object:
    def __init__(self, x, y, width, image, speed):
        self.x = x
        self.y = y
        self.width = width
        self.image = image
        self.speed = speed

    def move(self):
        # Кактус не вышел за экран
        if self.x >= -self.width:

            display.blit(self.image,(self.x,self.y))
            pygame.draw.rect(display, (106, 204, 45), (self.x, self.y, self.width, 50),5)
            self.x -= self.speed
            return True

        # Переместить кактус в правую часть экрана
        else:
            self.x = W + 100 + random.randint(-20,150)
            return False

    def return_self(self, radius, y, width, image):
        self.x = radius
        self.y = y
        self.width = width
        self.image = image
        
 
def jump():
    global  usr_y, jump_counter, make_jump
    if jump_counter >= -30:
        usr_y -= jump_counter / 2
        jump_counter -= 1
    else:
        jump_counter = 30
        make_jump = False


def run_game():
    global make_jump , dino_rect, bomb_rect , usr_x
    start_time = time.time() # Количество секунд с начала эпохи

    # pygame.mixer.music.play(-1)
    game = True
    cactus_arr = [] # Пустой список для кактусов
    create_cactus_arr(cactus_arr) # Заполнить список кактусов
    land = Object(0,0,800,land_img,4) # Первый фон
    land2 = Object(800,0,800,land_img,4) # Второй фон
    bomb = Object(200,250,70,bomb_image,4)
    
    cloud = open_random_object() # Создать облако
    cloud2 = open_random_object() # Создать облако
    
    while game:

        time_now = time.time() - start_time

        for event in pygame.event.get(): # Пройтись по всем событиям
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #Получение нажатых клавиш
        keys = pygame.key.get_pressed()
        if keys[K_SPACE]:
            make_jump = True

        if keys[K_ESCAPE]: # При нажатии ESCAPE поставить на паузу
            pause()
        if keys[K_a]:
            usr_x -= 5
        if keys[K_d]:
            usr_x += 5

        

        if make_jump:
            jump()

        display.fill((BG))
        
        # display.blit(land,(0,0))
        # display.blit(land.image, (land.x, land.y))
        # display.blit(land2.image, (land2.x, land2.y))


        move_objects(cloud,cloud2 , land, land2,bomb)
        # pygame.draw.rect(display, (255, 0, 0), bomb_rect)
        pygame.draw.rect(display, (255, 0, 0), dino_rect)
        dino_rect = dino_img[0].get_rect()
        print(dino_rect)
        dino_rect.x = usr_x
        dino_rect.y = usr_y

        # if bomb_rect.colliderect(dino_rect):
        #     print(True)
        draw_array(cactus_arr) # Рисовать кактусы
        # pygame.draw.rect(display,(225,200,0),(usr_x,usr_y,usr_width,usr_height))
        draw_dino()

        if check_collision(cactus_arr):
            game = False
        count_score(cactus_arr)
        print_text(f'Score: {score}', 10, 10, (255, 255, 255), 30)
        print_text(f'Max score: {max_score}', 10, 40, (255, 255, 255), 30)
        pygame.display.update()
        clock.tick(40)
    return game_over()

def create_cactus_arr(array):
    # Выбор случайных значений
    choice = random.randrange(0,3)
    img = cactus_img[choice]
    width = cactus_options[choice * 2]
    height = cactus_options[choice * 2 + 1]
    
    
    array.append(Object(W + 50, height, width, img, 4))
    array.append(Object(W + 300, height, width, img, 4))
    array.append(Object(W + 600, height, width, img, 4))
    


def find_radius(array):
    #Находение случайного положения
    maximum = max(array[0].x, array[1].x, array[2].x)
    if maximum < W :
        radius = W
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



def draw_array(array):
    for cactus in array:
        check = cactus.move()
        if not check:
            choice = random.randrange(0, 3)
            img = cactus_img[choice]
            width = cactus_options[choice * 2]
            height = cactus_options[choice * 2 + 1]
            
            #Переродить кактус в случайном месте
            #Найти случайный радиус появления
            radius = find_radius(array)
            # Установить радиус появления
            cactus.return_self(radius, height, width, img)

def draw_dino():
    global img_counter
    if img_counter == 12:
        img_counter = 0
    display.blit(dino_img[img_counter//6],(usr_x, usr_y) )
    pygame.draw.rect(display,(255,0,0),(usr_x,usr_y,usr_width,usr_height),5)
    img_counter += 1
    
    
    
def print_text(message, x, y, font_color = (0,0,0) ,font_size = 30 ):
    font_type = pygame.font.SysFont('Consolas', font_size )
    text =  font_type.render(message, True, font_color)
    display.blit(text, (x, y))

def pause():
    paused = True
    while paused:
    
        for event in pygame.event.get():  # Пройтись по всем событиям
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[K_RETURN]:
            paused =False

        print_text('Paused', W/2-80, 250, (255, 255, 0), 50)
        print_text('Press "Enter" to continue', W/2 - 220, 310, (255, 255, 0), 35)
        pygame.display.update()
        clock.tick(15)
        


def open_random_object():
    
    #Выбрать случайное облако
    choice = random.randrange(0,2)
    img_of_cloud = cloud_img[choice]
    
    #Создать облако
    cloud = Object(W + random.randrange(10,500,100), random.randrange(10,100), 70, img_of_cloud,1)
    return cloud

def move_objects(cloud ,cloud2 , land, land2, bomb):
    check = land.move()  # Когда на экране - результат True
    if not check:
        land.return_self(W, 0, land.width, land_img)
    
    check = land2.move()  # Когда на экране - результат True
    if not check:
        land2.return_self(W, 0, land2.width, land_img)

    check = cloud.move()
    # Если облако зашло за экран
    if not check:
        choice = random.randrange(0, 2)
        img_of_cloud = cloud_img[choice]
        cloud.return_self(W + random.randrange(50,500,10), random.randrange(10, 300,50), cloud.width, img_of_cloud)

    check = cloud2.move()
    # Если облако зашло за экран
    if not check:
        choice = random.randrange(0, 2)
        img_of_cloud = cloud_img[choice]
        cloud2.return_self(W + random.randrange(50,500,100), random.randrange(10, 300,50), cloud2.width, img_of_cloud)

    check = bomb.move()
    if not check:
        choice = random.randrange(0, 2)
        img_of_cloud = cloud_img[choice]
        cloud2.return_self(W + random.randrange(50,500,100), random.randrange(10, 300,50), cloud2.width, img_of_cloud)



def check_collision(barriers):
    for barrier in barriers:
        if usr_y + usr_height >= barrier.y:
            if barrier.x <= usr_x <= barrier.x + barrier.width:
                return True

            if barrier.x <= usr_x + usr_width <= barrier.x + barrier.width:
                return True

def count_score(barriers):
    global score,max_score, cactuses_counter

    for barrier in barriers:
        if barrier.x <= usr_x+usr_width <= barrier.x + barrier.width:
            if usr_y + usr_height <= barrier.y:
                if not barrier in  cactuses_counter :
                    cactuses_counter.append(barrier)

    if make_jump == False:
        score += len(cactuses_counter)
        cactuses_counter.clear()
        if score > max_score:
            max_score = score



def game_over():
    pygame.mixer.music.stop()
    stopped = True
    while stopped:


        for event in pygame.event.get():  # Пройтись по всем событиям
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[K_RETURN]:
            return True
        if keys[K_ESCAPE]:
            return False

        print_text(f'Max score:{max_score}', W / 2 - 100, 200, (255, 0, 0), 40)
        print_text('Game over', W / 2 - 100, 250, (255, 255, 0), 50)
        print_text('Press "Enter" to play again', W / 2 - 240, 310, (255, 255, 0), 35)
        print_text('"Esc" to close game', W / 2 - 150, 350, (255, 255, 0), 35)
        pygame.display.update()
        clock.tick(15)

while run_game():
    score = 0

pygame.quit()
quit()




