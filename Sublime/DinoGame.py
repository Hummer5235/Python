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

#Класс Cactus для создания подобных объектов
class Cactus:
   def __init__(self ,x,y, width , height , speed):
       #Конструктор
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
    # Функция для передвижения кактуса

   def move(self):
       if self.x >= -self.width:
           pygame.draw.rect(display,((120,225,14)),(self.x,self.y,self.width,self.height))
           self.x -=self.speed
       else:
           rand = random.randint(20, 150)
           self.x = display_width + 50 + rand


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

def run_game():
    global  make_jump
    game = True
    cactus_arr = []
    create_cactus_arr(cactus_arr)
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

        display.fill((255,255,255)) # Переменная display раздел set_mode
        draw_cactus_arr(cactus_arr)
        pygame.draw.rect(display,(247,240,22),(user_x,user_y,user_width,user_height))

        # draw_cactus()
        pygame.display.update()
        clock.tick(60)

# Функция jump() дял персонажа
def jump():
    global user_y , make_jump , jump_counter
    if jump_counter >= -30:
        user_y -= jump_counter
        jump_counter -=1
    else :
        jump_counter = 30
        make_jump = False

def create_cactus_arr(array):
    array.append(Cactus(display_width + 100 ,display_height - 160, 30, 60 , 4 ))
    array.append(Cactus(display_width + 800 ,display_height - 250, 20, 150 , 4 ))
    array.append(Cactus(display_width + 450 ,display_height - 220, 20, 120 , 4 ))

def draw_cactus_arr(array):
    for cactus in array:
        print(cactus.x, cactus.y)
        cactus.move()


# def draw_cactus():
#     global cactus_x,cactus_y,cactus_width,cactus_height
#
#     if cactus_x >= -cactus_width:
#         pygame.draw.rect(display,(120,225,14),(cactus_x,cactus_y,cactus_width,cactus_height))
#         cactus_x -=3
#     else:
#         cactus_x = display_width - 60
run_game()
