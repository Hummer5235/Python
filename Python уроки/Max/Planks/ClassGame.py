import pygame
import pygame as pg
import random
from pygame.locals import *

pygame.init()

screen = pg.display.set_mode((800, 600), RESIZABLE)
BALLSPEED = 2
BLOCKWIDTH,BLOCKHEIGHT =50,25
SCREEN_SIZE = 0


#sounds
break_sound = pygame.mixer.Sound('block-break.wav')
break_sound2 = pygame.mixer.music.load("Отскок.mp3")
game = None

class Bonus(pg.sprite.Sprite):
    def __init__(self,x,y):
        pg.sprite.Sprite.__init__(self)
        image = pg.image.load("potion.png")
        self.image = pg.transform.scale(image,(30,30))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.name = "BONUS"

    def update(self,*args):
        self.rect.y += 1
        if self.rect.y >= 600:
            self.kill()




class Block(pg.sprite.Sprite):
    def __init__(self,color = (87, 214, 242)):
        pg.sprite.Sprite.__init__(self)
        self.size = [BLOCKWIDTH,BLOCKHEIGHT]
        self.image = pg.Surface(self.size)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.name = "BLOCK"




class Ball(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((15, 15))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect(center=(400,300))
        self.score = 0
        self.isMoving = True
        self.speedx = BALLSPEED
        self.speedy = BALLSPEED
        self.name="BALL"

    def update(self, keys,platform,blocks,screen_size,*args):
        global game
        if self.isMoving :
            self.rect.y += self.speedy
            # Группа объектов доступных для коллизиии
            hitGroup = pg.sprite.Group(platform,blocks)

            # Список объектов которых мы коснулись в данный момент
            spriteHitList = pg.sprite.spritecollide(self,hitGroup,False)

            # При касании оттолкнуться
            if len(spriteHitList) > 0 :
                for sprite in spriteHitList:
                    spriteLeft =sprite.rect.left
                    spriteRight = sprite.rect.right
                    if sprite.name == "BLOCK":
                        pygame.mixer.music.play()
                        sprite.kill()
                        self.speedy *= -1
                        self.rect.y += self.speedy
                        self.score += 1

                    if sprite.name == "BONUS_BLOCK":
                        bonus = Bonus(self.rect.x, self.rect.y)
                        game.sprites.add(bonus)
                        pygame.mixer.music.play()
                        sprite.kill()
                        self.speedy *= -1
                        self.rect.y += self.speedy
                        self.score += 1

                    elif sprite.name == "PLATFORM":

                        self.speedy *= -1
                        self.rect.y += self.speedy

            print(self.score)
            #Создать сообщение о выигрыше
            if self.score == 3:

                print_text("YOU ARE A WINNER!",(255,255,255),50,350,300)

            self.rect.x += self.speedx

            if self.rect.x > screen_size[0]:
                self.speedx *= -1
                self.rect.right = screen_size[0]
            if self.rect.x < 0:
                self.speedx *= -1
                self.rect.left = 0
            if self.rect.y < 0:
                self.speedy *= -1
                self.rect.top = 0
            if self.rect.y > screen_size[1]:
                self.isMoving = False





class Platform(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((60,10))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.center=(400,500)
        self.name = "PLATFORM"
        self.pick_up = False
        self.cooldown = 100

    def update(self,keys,*args):
        global game
        if keys[K_a] and self.rect.x > 0 :
            self.rect.x -= 10
        if keys[K_d] and self.rect.right < 800:
            self.rect.x += 10


        spriteHitList = pg.sprite.spritecollide(self, game.sprites, False)

        if len(spriteHitList) > 0:
            for sprite in spriteHitList:
                if sprite.name == "BONUS":
                    sprite.kill()
                    self.image = pygame.transform.scale(self.image,(self.image.get_width()+50,self.image.get_height()))
                    self.rect = self.image.get_rect(center=(self.rect.centerx,self.rect.centery))
                    # self.image = pygame.Surface((self.rect.width+50,10))
                    # self.rect = self.image.get_rect(center=(self.rect.centerx,self.rect.centery))
                    # self.image.fill((255,0,0))
                    self.pick_up = True


                if self.pick_up:
                    self.cooldown -= 0.5

                    if self.cooldown == 0:
                        #вернуть размеры
                        self.image = pygame.transform.scale(self.image,(60, 10))
                        self.rect = self.image.get_rect(center=(self.rect.centerx,self.rect.centery))
                        self.cooldown = 100
                        self.pick_up = False


def print_text(text, text_col,font_size, x, y):
    FONT = pygame.font.SysFont("Consolas", font_size)
    img = FONT.render(text,True,text_col,(255,13,50))
    screen.blit(img,(x,y))



class Game:
    def __init__(self):
        self.score = 0
        self.game_over = 0
        self.sprites = pg.sprite.Group() # Создадим группу для добавления спрайтов
        self.platform = Platform() # Создаем объект класса Platform
        self.ball = Ball()
        self.sprites.add(self.platform) # Добавляем платформу в гуппу спрайтов
        self.sprites.add(self.ball)
        self.blocks = pg.sprite.Group()


        b = Bonus(400,400)
        self.sprites.add(b)


        #Сетка из блоков

        for row in range(5):
            for col in range(14):
                random_number = random.randint(1, 3)
                if random_number == 1 :
                    block = Block((41,50,67))
                    block.name = "BONUS_BLOCK"
                else:
                    block = Block()

                block.rect.x = 3 + col * (BLOCKWIDTH + 7)
                block.rect.y = 3+ row * (BLOCKHEIGHT + 7)
                self.blocks.add(block)


        self.sprites.add(self.blocks)

    def process_events(self):
        for event in pg.event.get():
            if event.type == QUIT:
                return True
            if event.type == MOUSEBUTTONDOWN:
                if self.game_over:
                    self.__init__()

    def run_logic(self):
        pass
    def display_frame(self,screen,keys):
        global SCREEN_SIZE

        screen.fill((0,0,0))
        self.sprites.update(keys,self.platform,self.blocks,SCREEN_SIZE)
        self.sprites.draw(screen)



        if self.ball.isMoving == False:
            pygame.quit()
            quit()








def main():
    global SCREEN_SIZE,game,screen
    pg.init()

    pg.display.set_caption("Arcanoid")

    endgame = False
    clock = pg.time.Clock()

    game = Game()

    while not endgame:

        SCREEN_SIZE = screen.get_size()

        endgame = game.process_events()
        game.run_logic()
        keys = pg.key.get_pressed()
        game.display_frame(screen,keys)
        print_text(str(game.ball.score),(255,255,255),50,700,500)




        clock.tick(60)
        pg.display.update()



main()