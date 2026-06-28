import  pygame, random
pygame.init() # Запуск
# Игра это бесконечный цикл
# Переменные для дисплея
display_width = 800
display_height = 600
display = pygame.display.set_mode((display_width,display_height)) # Установить размер дисплея
pygame.display.set_caption("Dino Game") # Установить надпись
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

cactus_img = [pygame.image.load("Cactus0.png"),
              pygame.image.load("Cactus1.png"),
              pygame.image.load("Cactus2.png")]

cactus_options = [69 , 449 , 37 , 410 , 40 , 420] # Высота дисплея  - 100 - высота кактуса

cloud_image = [pygame.image.load("Cloud0.png"),pygame.image.load("Cloud1.png")]
stone_image = [pygame.image.load("Stone0.png"),pygame.image.load("Stone1.png")]

dino_image = [pygame.image.load("Dino0.png"),
              pygame.image.load("Dino1.png"),
              pygame.image.load("Dino2.png"),
              pygame.image.load("Dino3.png"),
              pygame.image.load("Dino4.png")]
img_counter = 0

#Класс Cactus для создания подобных объектов
class Object:
    def __init__(self ,x,y, width , image, speed):
       #Конструктор
        self.x = x
        self.y = y
        self.width = width
        self.image = image
        self.speed = speed
    # Функция для передвижения кактуса

    def move(self):
       if self.x >= -self.width:
           display.blit(self.image,(self.x,self.y))
           # pygame.draw.rect(display,((120,225,14)),(self.x,self.y,self.width,self.height))
           self.x -=self.speed
           return True
       else:
            return False
           # self.x = display_width + 100 + random.randrange(-80,100)


    def return_self(self,radius , y , width, image): # Метод присваивает новое расстояние для х координаты объекта
        self.x = radius
        self.y = y
        self.width = width
        self.image = image
        # display.blit(self.image,(self.x,self.y))

# Фон
land = pygame.image.load("Land2.jpg")
land2_1 = pygame.image.load("Land2_1.jpg")
land_x = 0
land2_1_x = 800


#Создаем персонажа
user_width = 60
user_height = 100
user_x = display_width/8
user_y = display_height - 100 - user_height

#Враг
cactus_width = 20
cactus_height = 70
cactus_x = display_width - 60
cactus_y = display_height - 100 - cactus_height



#Обновление экрана
clock = pygame.time.Clock()

#Прыжок
make_jump = False
jump_counter = 30



def open_random_objects():
    choice = random.randrange(0,2)
    img_of_stone = stone_image[choice]

    choice = random.randrange(0,2)
    img_of_cloud = cloud_image[choice]

    stone = Object(display_width,display_height-80,10,img_of_stone,4)
    cloud = Object(display_width+100,80,70,img_of_cloud,1)

    return  stone,cloud

def move_object(stone,cloud):
    check = stone.move()
    if not check:
        choice = random.randrange(0,2)
        img_of_stone = stone_image[choice]
        stone.return_self(display_width,500+random.randrange(10,80),stone.width, img_of_stone )

    check = cloud.move()
    if not check:
        choice = random.randrange(0,2)
        img_of_cloud = cloud_image[choice]
        cloud.return_self(display_width,random.randrange(10,200),cloud.width, img_of_cloud )

def draw_dino():
    global img_counter
    if img_counter == 25:
        img_counter = 0
    display.blit(dino_image[img_counter//5],(user_x,user_y))
    img_counter += 1

def run_game():
    global  make_jump,land_x ,land2_1_x
    game = True

    cactus_arr = []
    create_cactus_arr(cactus_arr)

    stone , cloud = open_random_objects()
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        key = pygame.key.get_pressed()

        # Нажатие клавиши пробел и запуск функции прыжка
        if key[pygame.K_SPACE]:
            make_jump = True
        if make_jump:
            jump()

        # display.fill((255,255,255)) # Переменная display раздел set_mode
        land_x = draw_background(land,land_x)
        land2_1_x = draw_background(land2_1,land2_1_x)
        draw_cactus_arr(cactus_arr)
        move_object(stone,cloud)
        # user= pygame.draw.rect(display,(254,153,0),(user_x,user_y,user_width,user_height))
        draw_dino()

        # draw_cactus()
        pygame.display.update()
        clock.tick(60)

# Функция jump() для персонажа
def jump():
    global user_y , make_jump , jump_counter
    if jump_counter >= -30:
        user_y -= jump_counter
        jump_counter -=1
    else :
        jump_counter = 30
        make_jump = False

def create_cactus_arr(array):

    choice = random.randrange(0,3)
    img = cactus_img[choice]
    width = cactus_options[choice * 2]
    height = cactus_options[choice * 2 + 1]
    array.append(Object(display_width + 100, height, width, img, 4))

    choice = random.randrange(0,3)
    img = cactus_img[choice]
    width = cactus_options[choice * 2]
    height = cactus_options[choice * 2 + 1]
    array.append(Object(display_width + 350, height, width, img, 4))

    choice = random.randrange(0,3)
    img = cactus_img[choice]
    width = cactus_options[choice * 2]
    height = cactus_options[choice * 2 + 1]
    array.append(Object(display_width + 700, height, width, img, 4))


def find_radius(array):
    # Максимальное значение каждого элемента по "х" в момент перерисовки нового кактуса
    maximum = max(array[0].x,array[1].x,array[2].x)
    # Проверка где находится кактус
    if maximum < display_width:
        radius = display_width
        if radius - maximum <= 50:
            radius += 150
    else:
        radius = maximum

    choice = random.randrange(0,5)
    if choice == 0:
        radius += random.randrange(10,15)
    else:
        radius += random.randrange(200, 350)

    return radius




def draw_cactus_arr(array):
    for cactus in array:
        check = cactus.move() # Из метода move() возвращается True пока программа выполняется
        if not check: # Возвращается False , когда кактус ушел за границу экрана
            radius = find_radius(array)

            choice = random.randrange(0,3)
            img = cactus_img[choice]
            width = cactus_options[choice * 2]
            height = cactus_options[choice * 2 + 1]


            cactus.return_self(radius,height,width,img)

def draw_background(l,l_x):
    display.blit(l,(l_x,0))
    l_x -= 4
    if l_x <= - 800:
        l_x = 800
    return  l_x





run_game()

# def draw_cactus():
#     global cactus_x,cactus_y,cactus_width,cactus_height
#
#     if cactus_x >= -cactus_width:
#         pygame.draw.rect(display,(120,225,14),(cactus_x,cactus_y,cactus_width,cactus_height))
#         cactus_x -=3
#     else:
#         cactus_x = display_width - 60
