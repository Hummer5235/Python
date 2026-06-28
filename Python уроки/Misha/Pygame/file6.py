#Класс Rect - прямоугольник
import pygame
pygame.init()

W, H = 800, 500
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)



screen = pygame.display.set_mode((W,H),pygame.RESIZABLE)#Создание окна

pygame.display.set_caption('Класс Rect')
pygame.display.set_icon(pygame.image.load('Icon1.png'))


clock = pygame.time.Clock() # создай экз часы
FPS = 60
x = 400
y = 300
speed = 10

StartDraw = False

ground = H - 50 # высота земли
jump_force = 10 # сила прыжка
move = jump_force + 1 # текущая вертикальная скорость

player = pygame.Surface((150, 150))
rect1 = player.get_rect(centerx=W // 2)


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        move -= jump_force



    player.fill(BLUE)
    rect1.bottom = ground

    # rect1.move_ip(10,2) # меняет координаты текущего прямоугольника со смещениями x, y;



    screen.fill(BLACK)
    screen.blit(player,rect1)
    pygame.display.update()






     # Обновление дисплея
    clock.tick(FPS) #

