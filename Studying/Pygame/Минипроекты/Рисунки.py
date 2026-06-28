import sys

import pygame as pg
import sys



sc = pg.display.set_mode((800, 600))

running = True

clock = pg.time.Clock()

#Загрузить изображение
dog_img = pg.image.load('dog.jpg')
dog_img.set_colorkey((255,255,255))

#Получить прямоугольник для рисования и позиционирования на экране
dog_rect = dog_img.get_rect()
dog_img = pg.transform.scale(dog_img, (150, 150))


sc.blit(dog_img,dog_rect)

while running  :
    clock.tick(60)
    sc.fill((0,0,0))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            sys.exit()
        if event.type in (pg.MOUSEMOTION, pg.MOUSEBUTTONDOWN,pg.APPMOUSEFOCUS):
            x_pos, y_pos = pg.mouse.get_pos()
            dog_rect = dog_img.get_rect()

            sc.blit(dog_img,dog_img.get_rect(centerx=x_pos, centery=y_pos))

    pg.display.update()
