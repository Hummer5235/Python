import pygame as pg
from pygame.locals import*
from sys import exit
import time

# ООП - создание собственного типа данных, который
# обретает атрибуты, свойства и методы для работы с атрибутами

# Класс - шаблон
# Экземпляр - конкретный объект
# self - ссылка на текущий экземпляр


BALLSPEED=4
BLOCKWIDTH = 25  # Ширина блока
BLOCKHEIGHT = 15 # Высота блока


class Block(pg.sprite.Sprite):
	def __init__(self):
		pg.sprite.Sprite.__init__(self)
		self.size = [BLOCKWIDTH,BLOCKHEIGHT]
		self.image = pg.Surface(self.size)  # Создать поверхность
		self.image.fill((255, 255, 255)) # Залить цветом
		self.rect = self.image.get_rect()
		self.name = "BLOCK"










class Ball(pg.sprite.Sprite):
	def __init__(self):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.Surface((15,15))  # Создать поверхность
		self.image.fill((244, 247, 27)) # Залить цветом
		self.rect = self.image.get_rect(center=(400,400))
		self.score = 0  # Очки
		self.lifes = 3
		self.isMoving = True  # Флаг для проверки
		self.speedy =BALLSPEED*-1
		self.speedx = BALLSPEED*1 
		self.bounce = pg.mixer.Sound("bounce.wav")
		self.point = pg.mixer.Sound("goal.wav")
		self.lose = pg.mixer.Sound("lose.wav")
		self.game_over = pg.mixer.Sound("GameOver.wav")
		self.game_over2 = pg.mixer.Sound("GameOver2.wav")
		self.win = pg.mixer.Sound("Winner.wav")


	def update(self,keys,platform,blocks,*args):
		if self.isMoving:
			self.rect.y	+= self.speedy

			hitGroup=pg.sprite.Group(platform,blocks)#Группа спрайтов
			spriteHitList=pg.sprite.spritecollide(self,hitGroup,False)#Список колизий

			if len(spriteHitList) > 0:
				for sprite in spriteHitList:
					if sprite.name == "BLOCK":
						sprite.kill()
						self.point.play()
						self.score +=1
						
						self.speedy *= -1
						self.rect.y += self.speedy

					elif sprite.name =="PLATFORM":
						self.speedy *= -1	

			self.rect.x += self.speedx	 # Двигаться поsx

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
				if self.lifes >1:
					self.speedy *=-1
					self.rect.bottom = 600
					self.lifes -=1
					self.lose.play()
					time.sleep(1)
					self.rect.center =(400,400) 

				else:

					self.isMoving = False


				
					










class Platform(pg.sprite.Sprite):
	def __init__(self):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.Surface((60,10)) # Создание экземпляра класса Surface c опр размера
		self.rect = self.image.get_rect(center=(400,500)) 
		self.image.fill((255,0,0))
		self.name = "PLATFORM"

	def update(self,keys,*args):  # Управление платформой
		if keys[K_a] and self.rect.x>0 :             # Добавить границы
			self.rect.x -=10 
		if keys[K_d] and self.rect.x<800-self.rect[2]:
			self.rect.x += 10




class Game:
	def __init__(self): #Создание экземпляра класса
		self.score = 0
		self.game_over = 0
		self.sprites = pg.sprite.Group() # Создать класс для объединения спрайтов в группу
		self.platform = Platform() # Создать платформу
		self.sprites.add(self.platform) # Добавить платформу в группу спрайтов
		self.ball = Ball()   # Создать объект класса Ball
		self.sprites.add(self.ball) # Добавить ball в группу спрайтов
		self.blocks = pg.sprite.Group()
		self.font = pg.font.Font(None,32) # Добавить шрифт

		#Создание таблицы из блоков
		for row in range(10):
			for col in range(25):
				block = Block()
				block.rect.x = col * (BLOCKWIDTH +7 )
				block.rect.y = row * (BLOCKHEIGHT +7)
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
		screen.fill((0,0,0))
		score = self.font.render("Score: "+str(self.ball.score),1,(255,255,255))
		screen.blit(score,(20,550))
		lifes = self.font.render("Lifes: "+str(self.ball.lifes),1,(0,255,0))
		screen.blit(lifes,(700,550))
		self.sprites.update(keys,self.platform,self.blocks)
		self.sprites.draw(screen)
		if self.ball.isMoving == False:
			self.ball.game_over2.play()
			time.sleep(2)
			self.__init__()





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
		clock.tick(60)

if __name__ == "__main__":
	main()	