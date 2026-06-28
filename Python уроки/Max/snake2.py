import pygame
from pygame.locals import *
import time
import random

pygame.init()  # Инициализация модуля pygame
pygame.display.set_caption("Snake")  # Создание заголовка игры
W,H = 800,600
screen = pygame.display.set_mode((W, H))  # Создание поверхности игры
clock = pygame.time.Clock()
font = pygame.font.SysFont("consolas",40)
can = 0

head = Rect(400, 300, 30, 30)

# Звуки
pygame.mixer.music.load("kim-lightyear-angel-eyes-chiptune-edit-110226.mp3")
pygame.mixer.music.set_volume(0) # Задать громкость музыки
eat_sound = pygame.mixer.Sound("goal.wav")
eat_sound.set_volume(0.2)
lose_sound = pygame.mixer.Sound("Lose.wav")

play = True

local_time = 0

color = (255, 255, 255)
speed = 30
direction = [speed, 0]
game_points = 0
bonus_banana = False

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r, g, b)

def load_image(src,x,y,size=(30,30)):
    image = pygame.image.load(src)
    image = pygame.transform.scale(image,size)
    rect = image.get_rect(center=(x,y))

    transparent = image.get_at((0,0))
    image.set_colorkey(transparent)

    return image,rect


def move(head,snake):
    global direction, color, keys

    if keys[K_UP] and direction[1] == 0:
        direction = [0, -speed]
    elif keys[K_DOWN] and direction[1] == 0:
        direction = [0, speed]
    elif keys[K_LEFT]:
        direction = [-speed, 0]
    elif keys[K_RIGHT]:
        direction = [speed, 0]

    if head.bottom > 600:
        head.top = 0
    elif head.top < 0:
        head.bottom = 600
    elif head.left < 0:
        head.right = 800
    elif head.right > 800:
        head.left = 0



    for index in range(len(snake)-1,0,-1):
        snake[index].x = snake[index-1].x
        snake[index].y = snake[index - 1].y


    head.move_ip(direction)

def pickup(item):
    global apple_rect,head_rect, game_points ,snake,bonus_banana
    print(banana_rect.centerx)
    if head_rect.colliderect(item):
        item.x = random.randint(40,760)
        item.y = random.randint(40,560)
        if item == apple_rect:
            game_points += 1
            snake.append(snake[-1].copy())
        else:
            game_points += 2
            for i in range(2):
                snake.append(snake[-1].copy())
            bonus_banana=False
            item.x = W+200

        # print(f'Game_Points: {game_points}')
        eat_sound.play()

def show_banana():
    global bonus_banana,banana_rect
    number = random.randrange(0,500)
    if number == 95:
        bonus_banana = True
    if bonus_banana:
        banana_rect.x = random.randint(40, 760)
        banana_rect.y = random.randint(40, 560)
        screen.blit(banana_image,banana_rect)




def score():

    text = font.render(f"Score: {game_points}",1,(255,255,0)) # Создает поверхность и на ней печатает текст
    text_rect = text.get_rect(center=(400,500))
    screen.blit(text,text_rect)

def get_fonts():
    fonts_list = pygame.font.get_fonts()
    for i in fonts_list:
        print(i)
# get_fonts()

def game_over():
    for i in snake[1:]:
        if head_rect.colliderect(i):
            return True
    return False


x = random.randint(40,760)
y = random.randint(40,560)

head_image, head_rect = load_image("Images/head.png",500,100)
apple_image,apple_rect = load_image("Images/apple.png", 200,300)
body_image, body_rect = load_image("Images/body.png",470,100)
banana_image , banana_rect = load_image("Images/banana3.png",W+200,150,size=(55,55))

snake = [head_rect,body_rect]
pygame.mixer.music.play(-1) # Играть фоновую музыку

while play:
    for event in pygame.event.get():  # Проход по всем событиям
        if event.type == QUIT:  # Если мы нажали на крестик
            play = False

    screen.fill((0, 0, 0))
    # pygame.draw.rect(screen, color, head)

    keys = pygame.key.get_pressed()  # Получить нажатые клавиши
    screen.blit(head_image,head_rect)
    screen.blit(apple_image,apple_rect)
    show_banana()


    for segment in snake[1:]:
        screen.blit(body_image,segment)


    if game_over():
        pygame.mixer.music.stop()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(5)
            lose_sound.play()
        pygame.quit()
        quit()


    pickup(apple_rect)
    pickup(banana_rect)
    score()
    move(head_rect, snake)

    pygame.display.update()  # Обновить экран
    clock.tick(10)  # Замедляем игру до 60 фпс