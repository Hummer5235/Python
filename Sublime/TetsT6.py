import pygame
 
pygame.init()
 
W = 600
H = 400
 
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("События от клавиатуры")

 
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
FPS = 60        # число кадров в секунду
clock = pygame.time.Clock()
 
x = W // 2
y = H // 2
speed = 1
flLeft = flRight = False
 
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                flLeft = True
            elif event.key == pygame.K_RIGHT:
                flRight = True
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                flLeft = flRight = False
 
    if flLeft:
        x -= speed
    elif flRight:
        x += speed
 
    sc.fill(WHITE)
    pygame.draw.rect(sc, BLUE, (x, y, 10, 20))
    pygame.display.update()