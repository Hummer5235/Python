import pygame
import sys

FPS = 60
WIN_WIDTH = 400
WIN_HEIGHT = 100
WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)

clock = pygame.time.Clock()
sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

# радиус будущего круга
r = 30
# координаты круга
x = 0 - r  # скрываем за левой границей
y = WIN_HEIGHT // 2  # выравнивание по центру по вертикали





while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    sc.fill(WHITE)  # заливаем фон
    pygame.draw.circle(sc, ORANGE, (x, y), r)  # рисуем круг
    pygame.display.update()  # обновляем окно

    # Если круг полностью скрылся за правой границей,
    if x >= WIN_WIDTH + r:
        x = 0 - r  # перемещаем его за левую
    else:  # Если еще нет, на следующей итерации цикла
        x += 2  # круг отобразится немного правее

    clock.tick(FPS)