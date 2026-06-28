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

rect1 = pygame.Rect((0, 0, 30, 30)) #Создаем прямоугольник
rect2 = pygame.Rect((30, 30, 30, 30)) #Создаем прямоугольник

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    W, H = screen.get_rect().width, screen.get_rect().height
    print(screen.get_rect()) #Получить координаты
    player = pygame.Surface((150,150))
    rect = player.get_rect(topleft=(W/2,H/2))
    player2 = pygame.Surface((150,150))
    rect2 = player2.get_rect(center=(W/2,H/2))
    player3 = pygame.Surface((150,150))
    rect3 = player3.get_rect(bottomleft =(W/2,H/2))
    #Rect.Главные точки.Свойства
    #left/right
    #topleft/topright
    #bottomleft/bottomright
    #center
    #xy

    player.fill(BLUE)
    # player2.fill(RED)
    # player3.fill(YELLOW)
    # screen.blit(player2, rect2)
    # screen.blit(player, rect)
    # screen.blit(player3,rect3)
    rect1.move_ip(10,2) # меняет координаты текущего прямоугольника со смещениями x, y;
    screen.fill(BLACK)
    screen.blit(player,rect1)
    pygame.display.update()






     # Обновление дисплея
    clock.tick(FPS) #

