import pygame
import random
import math

pygame.init()

# Определяем цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Определяем размеры экрана
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Shoot 'em up!")

# Определяем класс для персонажа
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 50

    def move_left(self):
        self.rect.x -= 5

    def move_right(self):
        self.rect.x += 5

    def move_up(self):
        self.rect.y -= 5

    def move_down(self):
        self.rect.y += 5

# Определяем класс для пули
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, target_x, target_y):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5
        self.target_x = target_x
        self.target_y = target_y

    def update(self):
        # Вычисляем вектор направления пули
        dx = self.target_x - self.rect.x
        dy = self.target_y - self.rect.y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        vx = dx / distance
        vy = dy / distance

        # Перемещаем пулю по вектору
        self.rect.x += vx * self.speed
        self.rect.y += vy * self.speed

# Создаем группы спрайтов
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
bullets = pygame.sprite.Group()

running = True
clock = pygame.time.Clock()

# Основной игровой цикл
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = Bullet(player.rect.x, player.rect.y, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                bullets.add(bullet)
                all_sprites.add(bullet)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move_left()
    if keys[pygame.K_RIGHT]:
        player.move_right()
    if keys[pygame.K_UP]:
        player.move_up()
    if keys[pygame.K_DOWN]:
        player.move_down()

    # Обновляем все спрайты
    all_sprites.update()

    # Проверяем столкновение пуль с персонажами
    for bullet in bullets:
        hits = pygame.sprite.spritecollide(bullet, all_sprites, False)
        for hit in hits:
            if hit != bullet:
                all_sprites.remove(hit)
                all_sprites.remove(bullet)
                bullets.remove(bullet)

    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()