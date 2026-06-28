import pygame as pg
from pygame.locals import*
from sys import exit

# ООП - создание собственного типа данных, который
# обретает атрибуты, свойства и методы для работы с атрибутами

# Класс - шаблон
# Экземпляр - конкретный объект
# self - ссылка на текущий экземпляр

class Platform(pg.sprite.Sprite):
	def __init__(self):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.Surface((60,10)) # Создание изображения. Surface - класс
		self.rect = self.image.get_rect(center=(400,590)) # Берем размеры и позицию центра 
		self.image.fill((255,0,0))

	def update(self,keys,*args):
		if keys[K_a] and self.rect.x >0:
			self.rect.x -=15
		if keys[K_d] and self.rect.right < 800:
			self.rect.x +=15


class Game:
	def __init__(self): #Создание экземпляра класса
		self.score = 0
		self.game_over = 0
		self.sprites = pg.sprite.Group() # Высокоуровневая обертка  
		platform = Platform()
		self.sprites.add(platform)



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
		self.sprites.update(keys)
		self.sprites.draw(screen)



def main():
	global a1
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
		pg.display.update()
		clock.tick(60)

if __name__ == "__main__":
	main()	 