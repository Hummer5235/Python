
import pygame
import random
import time

pygame.init()

#Размеры экрана
display_width = 800
display_height = 600
display = pygame.display.set_mode((display_width,display_height)) # Установить размеры экрана
pygame.display.set_caption("Run Dino! Run!") # Установить название

icon = pygame.image.load("app_icon.png") # Загрузить изображение
pygame.display.set_icon(icon) # Установить иконку

#Звуки
pygame.mixer.music.load("Pygame Materials/Sounds/Background_space.mp3")
pygame.mixer.music.set_volume(0.3)

lose_sound = pygame.mixer.Sound('Pygame Materials/Sounds/lose.wav') # Звук проигрыша
button_sound =pygame.mixer.Sound('Pygame Materials/Sounds/button.wav') # Звук кнопки

land_img = pygame.image.load("Pygame Materials/Backgrounds/Land2.jpg")  # Заданий фон

cactus_img = [pygame.image.load("Pygame materials/Objects/Cactus0(2).png"),
              pygame.image.load("Pygame materials/Objects/Cactus1(2).png"),
              pygame.image.load("Pygame materials/Objects/Cactus2(2).png")]

cloud_img = [pygame.image.load("Pygame Materials/Objects/Cloud0.png"),
             pygame.image.load("Pygame Materials/Objects/Cloud1.png")]

stone_img = [pygame.image.load("Pygame Materials/Objects/Stone0.png"),
             pygame.image.load("Pygame Materials/Objects/Stone1.png")]

dino_img=[pygame.image.load("Pygame Materials/Dino/DinoRun1.png"),
          pygame.image.load("Pygame Materials/Dino/DinoRun2.png")]

health_img = pygame.image.load("Pygame Materials/Effects/heart.png")
health_img = pygame.transform.scale(health_img,(40,40))

health = 3

#Счетчик для изображений
img_counter = 0

cactus_options = [68,452,36,412,40,420] # Параметры кактусов

class Object:
    def __init__(self,x,y,width,image,speed):
        self.x = x
        self.y = y
        self.width = width # Ширина
        self.speed = speed # Скорость
        self.image = image # Изображение

    def move(self):
        if self.x >= - self.width:
            display.blit(self.image,(self.x,self.y)) # Отрисовка движения кактуса
            # pygame.draw.rect(display, (230, 150, 0), (self.x, self.y, self.width, self.height))
            self.x -= self.speed  # Сместить кактус влево
            return True

        else:
            #self.x = display_width + 100 + random.randint(-80,80)
            return False

    def return_self(self,radius,y,width,image):
        self.x = radius
        self.y = y
        self.width = width
        self.image = image

class Button():
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.inactive_color = (0,0,0)
        self.active_color= (255,255,255)

    def draw(self,x,y,message,action = None,font_size =30):
        # Получить координаты мышки
        mouse = pygame.mouse.get_pos()
        #Получить нажатие мышки
        click = pygame.mouse.get_pressed()
        if x < mouse[0] < x + self.width and  y <mouse[1] < y + self.height:
            pygame.draw.rect(display,self.active_color,(x,y,self.width,self.height))
            if click[0]==True:
                button_sound.play()
                pygame.time.delay(100)
                if action is not None:
                    if action == quit:
                        pygame.quit()
                        quit()
                    else:
                        action()
        else:
            pygame.draw.rect(display, self.inactive_color, (x, y, self.width, self.height))

        print_text(message,x+10,y+10,font_size = font_size)

#Персонаж
usr_width = 60   # Ширина персонажа
usr_height = 95 # Высота персонажа
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

#Очки
score = 0
max_score = 0

cactuses_counter = [] # Счетчик кактусов


def game_cycle():
    global make_jump
    game = True
    cactus_arr = [] # Пустой список для кактусов
    create_cactus_arr(cactus_arr) # Заполнить список кактусов
    land = Object(0,0,800,land_img,4) # Фон_1
    land2 = Object(display_width,0,800,land_img,4) # Фон 2
    stone,cloud = open_random_object() # Создать камень и облако
    pygame.mixer.music.play(-1) # Играть музыку
    heart = Object(display_width,280,30,health_img,4)


    while game:
        for event in pygame.event.get(): # Пройтись по всем событиям
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed() # Получить кортеж нажатых клавиш
        if keys[pygame.K_SPACE]: # Если нажата клавиша пробел
            make_jump = True   # Разрешить прыжок

        if keys[pygame.K_ESCAPE]: # Если нажата клавиша Esc
            pause()
        if make_jump:
            jump()

        # display.blit(land,(0,0))
        move_objects(stone, cloud, land, land2)
        draw_array(cactus_arr) # Отрисовать список
        
        print_text(f"Score: {score} ", 600, 30)


        draw_dino() # Отрисовка динозаврика
        heart.move()
        hearts_plus(heart)
        if check_collision(cactus_arr): # Проверить столкновение
                game = False
        show_health()
        count_score(cactus_arr) # Подсчет очков
        pygame.display.update() # Обновить дисплей
        clock.tick(60)
    return game_over()

def jump():
    global  usr_y,jump_counter ,make_jump
    if jump_counter >= -30:
        usr_y -= jump_counter / 2 # Поднимаем вверх на jump_counter
        jump_counter -= 1 # Уменьшаем jump_counter ( Замедляем прыжок)
    else:
        # Как только опустились на землю (jump_counter >= -30) вернуть все значения вначало
        jump_counter = 30
        make_jump = False


#Создать массив кактусов
def create_cactus_arr(array):
    choice = random.randrange(0,3)  # Случайное число
    img = cactus_img[choice]  # Cлучайное изображение
    width = cactus_options[choice * 2]
    height = cactus_options[choice * 2 + 1]

    array.append(Object(display_width + 50, height, width, img, 4))
    array.append(Object(display_width + 300, height, width, img, 4))
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
            object_return(array,cactus)


def object_return(objects,object):
    radius = find_radius(objects)  # Найти радиус

    choice = random.randrange(0, 3)  # Случайное число
    img = cactus_img[choice]  # Cлучайное изображение
    width = cactus_options[choice * 2]
    height = cactus_options[choice * 2 + 1]

    object.return_self(radius, height, width, img)  # Вернуть себя

# Создание камней и облаков
def open_random_object():
    choice = random.randrange(0,2)
    img_of_stone = stone_img[choice]

    choice = random.randrange(0, 2)
    img_of_cloud = cloud_img[choice]

    stone = Object(display_width,display_height - 80,10,img_of_stone,4)
    cloud = Object(display_width, 80,70,img_of_cloud,1)

    return stone,cloud


def move_objects(stone,cloud,land,land2):

    check = land.move()  # Когда на экране - результат True
    if not check:
        land.return_self(display_width, 0, land.width, land_img)

    check = land2.move()  # Когда на экране - результат True
    if not check:
        land2.return_self(display_width, 0, land2.width, land_img)


    check = stone.move() # Когда на экране - результат True
    if not check:
        choice = random.randrange(0, 2)
        img_of_stone = stone_img[choice]
        stone.return_self(display_width,500+random.randrange(10, 80),stone.width,img_of_stone)

    check = cloud.move()  # Когда на экране - результат True
    if not check:
        choice = random.randrange(0, 2)
        img_of_cloud = cloud_img[choice]
        cloud.return_self(display_width, random.randrange(10, 200), cloud.width, img_of_cloud)

#Отрисовка динозаврика
def draw_dino():
    global img_counter

    if img_counter == 20:
        img_counter = 0

    display.blit(dino_img[img_counter//10],(usr_x,usr_y))
    if not make_jump:
        img_counter+=1


def print_text(message,x,y,font_color = (255,255,0), font_type ="Pygame materials/Fonts/minecraft.ttf",font_size= 30):
    font_type = pygame.font.Font(font_type,font_size) #
    text = font_type.render(message,True,font_color) # Формируем слой Surface для отрисовки текста
    display.blit(text,(x,y))


def pause():
    pygame.mixer.music.pause()
    paused = True
    start_time = time.perf_counter() # Начало отсчета
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]: # Если нажата клавиша Enter
            paused= False

        display.fill((0, 0, 0))
        local_time = time.perf_counter() - start_time # Разница во времени
        print_text(str(round(local_time)), 400, 250,font_size=25)
        print_text("Paused. Press Enter to continue",110,300)


        pygame.display.update()
        clock.tick(15)
    pygame.mixer.music.unpause()


def check_collision(barriers):

    for barrier in barriers:
        if usr_y+usr_height -20 >= barrier.y:
            if barrier.x <= usr_x + 15 <= barrier.x+barrier.width:
                if not check_health():
                    return True
                else:
                    object_return(barriers,barrier)


            elif barrier.x <= usr_x + usr_width -5 <= barrier.x+barrier.width:
                if not check_health():
                    return True
                else:
                    object_return(barriers, barrier)


def count_score(barriers):
    global score,cactuses_counter

    for barrier in barriers:
        if barrier.x <= usr_x+usr_width/2 <= barrier.x+barrier.width:
            if usr_y +usr_height -5 <= barrier.y:
                if not barrier in cactuses_counter:
                    cactuses_counter.append(barrier)

        if jump_counter==-30:
            score += len(cactuses_counter)
            cactuses_counter.clear()





def game_over():
    global score,max_score
    if score > max_score:
         max_score= score
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(lose_sound)

    stopped = True
    start_time = time.perf_counter()  # Начало отсчета
    while stopped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:  # Если нажата клавиша Enter
            return True

        if keys[pygame.K_ESCAPE]:
            return False


        # display.fill((0, 0, 0))
        local_time = time.perf_counter() - start_time  # Разница во времени
        print_text(str(round(local_time)), 400, 250, font_size=25)
        print_text("Game Over.  Press Enter to play again, Esc to exit.", 50, 300,font_size=25)
        print_text(f"Max score: {max_score}",300,350)

        pygame.display.update()
        clock.tick(15)


def show_health():
    #Рисование жизней
    global health
    show = 0
    x = 20
    while show != health:
        display.blit(health_img,(x,30))
        x += 40
        show += 1

def check_health():
    # Проверка жизней
    global health
    health -= 1
    if health == 0:
        return False
    else:
        return True

def hearts_plus(heart):
    global health,usr_x,usr_y,usr_width,usr_height

    if heart.x <= heart.width:
        radius = display_width + random.randrange(500, 1000)
        heart.return_self(radius, random.randrange(250,470), heart.width, heart.image)

    if usr_x <= heart.x <= usr_x+usr_width:
        if usr_y <= heart.y <= usr_y+usr_height:
            # pygame.mixer.Sound.play(heart_plus_sound)
            if health < 5:
                health += 1
            radius = display_width + random.randrange(1000,3000)
            heart.return_self(radius,random.randrange(250,470),heart.width,heart.image)

def show_menu():
    menu_bckgr = pygame.image.load("Pygame Materials/Backgrounds/Backgr3.png")
    menu_bckgr = pygame.transform.scale(menu_bckgr,(800,600))
    start_button = Button(275, 50)
    quit_button = Button(105,50)

    show = True
    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        display.blit(menu_bckgr,(0,0))
        start_button.draw(280,200,"Start Game",start_game,40)
        quit_button.draw(350,300,"Quit",quit,40)
        pygame.display.update()
        clock.tick(60)


def start_game():
    global score,health,cactuses_counter,make_jump,jump_counter,usr_y
    while game_cycle():
        score = 0
        make_jump = False
        health = 3
        cactuses_counter = []
        jump_counter = 30
        usr_y = display_height- 100 - usr_height

show_menu()

























