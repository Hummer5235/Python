import pygame, random
from datetime import *
pygame.font.init()

W,H = 800, 600

screen = pygame.display.set_mode((W,H))
clock = pygame.time.Clock()


text = pygame.font.Font(None, 36).render('Score',True,(255,0,0))

player_image = pygame.image.load('images/2.png')
player_image = pygame.transform.scale(player_image,(40,90))
player_rect = player_image.get_rect(center = (W//2,H-50))
bullet_image = 'images/bullet.png'
enemy_image ='images/enemy2.png'

enemy_images_list = ['images/enemy2.png','images/enemy2.2.png','images/enemy2.2.png']

bullet_cooldown = 0
b1 = 0
bullet_exists = False





#Группы спрайтов
bullets = pygame.sprite.Group() # Группа пуль




def cooldown():
    global bullet_cooldown
    if bullet_cooldown == 0:
        bullet_cooldown = 20
    if bullet_cooldown > 0 :
        bullet_cooldown -= 1





def check_keys():
    global player_direction, b1, bullet_cooldown
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if player_rect.y > 0:
            player_rect.y -= 5

    if keys[pygame.K_s]:
        if player_rect.y + player_image.get_height() < H:
            player_rect.y += 5
    if keys[pygame.K_a]:
        if player_rect.x > 0:
            player_rect.x -= 5
            player_direction = False
    if keys[pygame.K_d]:
        if player_rect.x + player_image.get_width() < W:
            player_rect.x += 5
            player_direction = True

    if keys[pygame.K_SPACE]:
        if bullet_cooldown == 0:
            b1 = Bullet(player_rect.x, player_rect.y, bullet_image)
            bullets.add(b1) # Добавить спрайт в группу
            bullet_exists = True
    cooldown()
    return b1

#Класс Пуля
class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.scale(self.image,(15,15))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.y -= 5



        if self.rect.y <= -10: # Уничтожить пулю при выходе за границу
            self.kill()



# b1 = Bullet(player_rect.x, player_rect.y, bullet_image)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_counter = 0
        self.direction = 'Right'
        self.idle = False
        self.choose_number = True
        self.damage = False
        self.animation_counter = 0
        self.image_cooldown = 0

    def update(self):
        screen.blit(self.image, self.rect)

        if pygame.sprite.spritecollide(self,bullets,True):
            self.damage = True
        if self.damage:
            self.take_damage()

    def take_damage(self):
        if self.animation_counter < 3:
            if self.image_cooldown <= 50:
                self.image_cooldown +=1
                self.image = pygame.image.load(enemy_images_list[self.image_cooldown//25])
                self.image = pygame.transform.scale(self.image, (70, 70))
            else:
                self.image_cooldown = 0
                self.animation_counter +=1
        else:
            self.damage = False
            self.animation_counter = 0
            self.image = pygame.image.load(enemy_images_list[0])
            self.image = pygame.transform.scale(self.image, (70, 70))

    def enemy_ai(self):

        r = None
        if self.idle == True :
            r = random.randint(1,50)

        if r == 1 and self.move_counter == 0:
            self.idle = False
            random2 = random.randint(1, 2)
            if random2 == 2:
                self.direction = 'Right'
            else:
                self.direction = 'Left'

        if self.idle == False:

            if self.move_counter < 200 :
                self.move_counter+= 1
                if self.direction == 'Right':
                    self.rect.x += 2
                else:
                    self.rect.x -= 2
            else:
                self.move_counter = 0
                self.idle = True

        if self.rect.x + 50 >= W:
            self.direction = 'Left'
        if self.rect.x - 50 <= 0:
            self.direction = 'Right'

        # print(self.move_counter)


enemy = Enemy(300,50, enemy_image)

Play = True
while Play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            Play = False



    check_keys()
    screen.fill((0,0,0))
    screen.blit(text,(50,50))
    #Рисование объектов
    bullets.draw(screen)
    bullets.update()
    enemy.update()
    enemy.enemy_ai()

    screen.blit(player_image,player_rect)

    clock.tick(60)
    pygame.display.update()
