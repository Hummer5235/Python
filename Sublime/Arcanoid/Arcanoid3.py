import pygame as pg
from pygame.locals import*
from sys import exit

# ООП - создание собственного типа данных, который
# обретает атрибуты, свойства и методы для работы с атрибутами

# Класс - шаблон
# Экземпляр - конкретный объект
# self - ссылка на текущий экземпляр


BALLSPEED=10

class Ball(pg.sprite.Sprite):
	def __init__(self):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.Surface((15,15))  # Создать поверхность
		self.image.fill((244, 247, 27)) # Залить цветом
		self.rect = self.image.get_rect(center=(200,200))
		self.score = 0  # Очки
		self.isMoving = True  # Флаг для проверки
		self.speedy =BALLSPEED
		self.speedx = BALLSPEED

	def update(self,keys,platform,*args):
		if self.isMoving:
			self.rect.y	+= self.speedy

			hitGroup=pg.sprite.Group(platform)#Группа спрайтов
			spriteHitList=pg.sprite.spritecollide(self,hitGroup,False)#Список колизий

			if len(spriteHitList) > 0:
				self.speedy *= -1
				self.rect.y += self.speedy
			self.rect.x += self.speedx	 # Двигаться по x

			#Устанавливаем границы

			#Правая граница
			if self.rect.right > 800:
				self.speedx *= -1
				self.rect.right = 800
			#Левая граница
			if self.rect.left < 0:
				self.speedx *= -1
				self.rect.left = 0
			#Вехняя граница
			if self.rect.top < 0:
				self.speedy *= -1
				self.rect.top = 0

			if self.rect.bottom > 600:
				self.speedy *= -1
				self.rect.bottom = 600








class Platform(pg.sprite.Sprite):
	def __init__(self):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.Surface((60,10)) # Создание экземпляра класса Surface c опр размера
		self.rect = self.image.get_rect(center=(400,500)) 
		self.image.fill((255,0,0))

	def update(self,keys,*args):  # Управление платформой
		if keys[K_a] and self.rect.x>0 :             # Добавить границы
			self.rect.x -=15 
		if keys[K_d] and self.rect.x<800-self.rect[2]:
			self.rect.x += 15




class Game:
	def __init__(self): #Создание экземпляра класса
		self.score = 0
		self.game_over = 0
		self.sprites = pg.sprite.Group() # Создать класс для объединения спрайтов в группу
		self.platform = Platform() # Создать платформу
		self.sprites.add(self.platform) # Добавить платформу в группу спрайтов
		ball = Ball()   # Создать объект класса Ball
		self.sprites.add(ball) # Добавить ball в группу спрайтов




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
		screen.fill((0,0,0))
		self.sprites.update(keys,self.platform)
		self.sprites.draw(screen)




def main():
	
	pg.init()

	pg.display.set_caption("Arcanoid")
	screen =pg.display.set_mode((800,600))
	
	
	
	endgame= False
	clock = pg.time.Clock()

	game = Game()

	while not endgame:
		endgame = game.process_events()
		game.run_logic()
		keys = pg.key.get_pressed()
		game.display_frame(screen,keys)
		# screeball.update(screen)n.fill((0,0,0))
		pg.display.update()
		clock.tick(30)

if __name__ == "__main__":
	main()	