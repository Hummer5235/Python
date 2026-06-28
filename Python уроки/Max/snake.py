import pygame
from pygame.locals import *
import time
import random



pygame.init() # Инициализация модуля pygame
pygame.display.set_caption("Snake") # Создание заголовка игры
screen = pygame.display.set_mode((800,600)) # Создание поверхности игры
clock = pygame.time.Clock()

head = Rect(400,300,30,30)

play = True

color = (255,255,255)
speed = 2
direction = [speed, 0]

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

def move(head):
    global direction,color , keys

    if keys[K_UP]:
        direction = [0, -speed]
    elif keys[K_DOWN]:
        direction = [0, speed]
    elif keys[K_LEFT]:
        direction = [-speed, 0]
    elif keys[K_RIGHT]:
        direction = [speed, 0]
        
    if head.bottom > 600:
        direction = [0,-speed]
        color = random_color()
    elif head.top <0:
        direction = [0,speed]
        color = random_color()
    elif head.left < 0:
        direction = [speed,0]
        color = random_color()
    elif head.right > 800:
        direction = [-speed,0]
        color = random_color()

    head.move_ip(direction)






while play:
    for event in pygame.event.get(): # Проход по всем событиям
        if event.type == QUIT: # Если мы нажали на крестик
            play = False

    # screen.fill((0, 0, 0))
    pygame.draw.rect(screen,color,head)

    keys = pygame.key.get_pressed() # Получить нажатые клавиши



    move(head)


    pygame.display.update()  # Обновить экран
    clock.tick(60)  # Замедляем игру до 60 фпс