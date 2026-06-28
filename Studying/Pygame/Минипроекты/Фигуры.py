import pygame as pg
import sys
from random import randint

screen = pg.display.set_mode((800, 600))

# Создание окна
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("Фигуры")

#Частота кадров в секунду
FPS = 60
clock = pg.time.Clock()

# Бесконечный цикл
running = True

while running:
    # Обработка событий
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            pos = pg.mouse.get_pos()
            pos_x = pos[0]
            pos_y = pos[1]
            print('Нажал', pos_x, pos_y)
            # random = randint(0,255)
            pg.draw.circle(screen, (randint(0,255), randint(0,255), randint(0,255)), (pos_x, pos_y), 50, 5)
        if event.type == pg.QUIT:
            sys.exit()
            running = False  # Выход из цикла при закрытии окна

    clock.tick(FPS)
    pg.display.update()