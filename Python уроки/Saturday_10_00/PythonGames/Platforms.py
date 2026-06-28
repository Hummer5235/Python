import sys

import pygame
from pygame.locals import *

BALLSPEED = 2
BLOCKWIDTH = 71
BLOCKHEIGHT = 50

#Цвета
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
YELLOW = (255,255,0)
RED = (255,0,0)
Brown = (94, 67, 47)


class Block(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.size = [BLOCKWIDTH,BLOCKHEIGHT]
        self.image = pygame.Surface(self.size)
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.name = 'Block'

class Ball(pygame.sprite.Sprite):
    #Наследуем свойства и методы из класса sprite
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20,20))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.y = 530
        self.rect.x = 400
        self.speedx = BALLSPEED
        self.speedy = -BALLSPEED
        self.score = 0
        self.isMoving = True

    def update(self,keys,platform,blocks,*args):
        if self.isMoving :
            hitGroup = pygame.sprite.Group(platform,blocks) # Создаем группу
            spriteHitList = pygame.sprite.spritecollide(self, hitGroup, False) # Проверяем столкновение

            if len(spriteHitList) > 0: # Если с кем-то столкнулись, то развернуться
                self.speedy *= -1
                self.rect.y += self.speedy
                for sprite in spriteHitList:
                    if sprite.name == 'Block':
                        sprite.kill() #Уничтожить спрайт
                        self.score += 1
                        print(self.score)



            if self.rect.right > 800: #Когда подошел правой стороной к краю, поменяй направление
                # self.rect.right = 800
                self.speedx *= - 1
            if self.rect.left < 0: #Когда подошел левой стороной к краю, поменяй направление
                # self.rect.left = 0
                self.speedx *= - 1
            if self.rect.top <0:
                # self.rect.top = 0
                self.speedy *= -1
            if self.rect.bottom >620:
                # self.rect.bottom = 600
                # self.speedy *= -1
                self.isMoving = False
                print('Конец игры')

            self.rect.x += self.speedx
            self.rect.y += self.speedy


class Platform(pygame.sprite.Sprite):
    # Наследуем свойства и методы из класса sprite
    def __init__(self):
        # self.screen = screen
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/Platform1.png') #загрузить картинку
        self.image = pygame.transform.scale(self.image,(70,20)) #изменить размер картинки
        self.rect = self.image.get_rect(x=350,y = 550) #сохранить координаты картинки
        self.name = 'Platform'
        # print(self.rect.width,self.rect.height)

    def update(self,keys,*args):
        # print('update')
        if keys[K_d] and self.rect.x < 730 :
            self.rect.x += 5
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= 5
        elif keys[K_SPACE ]:
            print('Space нажата')


        # self.rect.x += 1
        # self.rect.y += 1
        # self.screen.blit(self.image,(100,100))
        pass


class Game:
    def __init__(self):
        self.score = 0
        self.game_over = 0
        self.sprites = pygame.sprite.Group() #Создаем группу спрайтов
        self.platform = Platform()
        self.ball = Ball()
        self.sprites.add(self.ball)
        self.sprites.add(self.platform) #Добавляем платформу в группу спрайтов
        self.blocks = pygame.sprite.Group() # Создаем группу блоков


        #Строим сетку блоков
        for row in range(5):
            for col in range(10):
                block = Block()
                block.rect.x = col * (BLOCKWIDTH + 10) # 0 * 50+10
                block.rect.y = row * (BLOCKHEIGHT + 10) # 2 * 60+10
                self.blocks.add(block)
        self.sprites.add(self.blocks)



    def process_events(self): # Перебор событий игры
        # print('События')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

    def run_logic(self):
       # print('Логика')
       pass

    def display_frame(self,screen,keys):
        screen.fill((0, 0, 0))
        score = pygame.font.SysFont('Consolas',32).render(f'Score: {self.ball.score}',1,YELLOW)
        screen.blit(score,(0,570))
        self.sprites.draw(screen) # Нарисовать все спрайты
        self.sprites.update(keys,self.platform,self.blocks) # Обновить все спрайты
        if self.ball.isMoving == False:
            score = pygame.font.SysFont('Consolas', 100).render(f'Game Over', 1, YELLOW)
            screen.blit(score, (160, 300))
            score = pygame.font.SysFont('Consolas', 40).render(f'Enter to restart/ Esc to exit', 1, RED)
            screen.blit(score, (70, 420))
            KEYS = pygame.key.get_pressed()
            if KEYS[K_RETURN] :
                self.__init__() # Game запустить себя.__init__ заново
            elif KEYS[K_ESCAPE]:
                sys.exit()

        pygame.display.update()





#Главная функция
def main():
    pygame.init()
    W,H = 800,600
    screen = pygame.display.set_mode((W,H))
    pygame.display.set_caption('Platforms')

    game = Game()
    endgame = False
    clock = pygame.time.Clock()

    while not endgame:
        endgame = game.process_events()
        keys = pygame.key.get_pressed()  # Получить список нажатых клавиш
        game.run_logic()
        game.display_frame(screen,keys)


        clock.tick(80)
main()