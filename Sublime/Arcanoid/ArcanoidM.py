import pygame as pg 
from pygame.locals import *


BALLSPEED = 10
class Ball(pg.sprite.Sprite):
	def __init__(self):
		pg.sprite.Sprite.__init__(self)
		self.image=pg.Surface((15,15))
		self.image.fill((3,0,199))
		self.rect=self.image.get_rect(center=(400,700))
		self.score=0
		self.isMoving=True
		self.speedx=BALLSPEED
		self.speedy=BALLSPEED * -1

	def update(self,keys,platform,*args):
		if self.isMoving:
			self.rect.y	+= self.speedy

			hitGroup=pg.sprite.Group(platform)#Группа спрайтов
			spriteHitList=pg.sprite.spritecollide(self,hitGroup,False)#Список колизий

			if len(spriteHitList) > 0:
				self.speedy *= -1
				self.rect.y += self.speedy
			self.rect.x += self.speedx	


class Platform(pg.sprite.Sprite):
	def __init__(self):
		pg.sprite.Sprite.__init__(self)
		self.image=pg.Surface((60,10))
		self.rect=self.image.get_rect(center=(400,500))
		self.image.fill((255,0,0))

	def update(self,keys,*args):
		if keys[K_a] and self.rect.x > 0: # Добавить ограничение движения платформы
			self.rect.x -=15
		if keys[K_d]:
			self.rect.x +=15	


class Game():
	def __init__(self):
		self.score=0
		self.game_over=0
		self.sprites = pg.sprite.Group()
		self.platform = Platform()
		self.sprites.add(self.platform)
		ball = Ball()
		self.sprites.add(ball)






	def procces_events(self):
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

	W,H = 800,600
	pg.display.set_caption("Arcanoda 3000 500 #Super Game")
	screen = pg.display.set_mode((W,H))

	endgame = False
	clock=pg.time.Clock()

	game = Game()



	while not endgame:
		
		endgame = game.procces_events()
		game.run_logic()
		keys=pg.key.get_pressed()
		pg.display.update()
		game.display_frame(screen,keys)

		clock.tick(60)
								
if __name__ == "__main__":
	main()