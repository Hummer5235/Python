import pygame as pg
from pygame.locals import*
from sys import exit

# ООП - создание собственного типа данных, который
# обретает атрибуты, свойства и методы для работы с атрибутами

# Класс - шаблон
# Экземпляр - конкретный объект
# self - ссылка на текущий экземпляр



class Game:
	def __init__(self): #Создание экземпляра класса
		self.score = 0
		self.game_over = 0

	def process_events(self):
		for event in pg.event.get():
			if event.type == QUIT:
				return True
			if event.type == MOUSEBUTTONDOWN:
				if self.game_over:
					self.__init__()

	def run_logic(self):
		pass

	def display_frame(self,screen):
		pass

class Ball:
	
	def __init__(self,x,y,speed_x,speed_y):
		self.x = x
		self.y = y
		self.speed_x = speed_x
		self.speed_y = speed_y
		self.image = pg.image.load("ball.png")
		self.image = pg.transform.scale(self.image,(30,30))
		self.rect = self.image.get_rect()

	def update(self,screen):
		self.x+=self.speed_x
		self.y+=self.speed_y
		screen.blit(self.image,(self.x,self.y))

def main():
	
	pg.init()

	pg.display.set_caption("Arcanoid")
	screen =pg.display.set_mode((800,600))
	
	ball = Ball(200,300,15,15)
	
	
	
	endgame= False
	clock = pg.time.Clock()

	game = Game()

	while not endgame:
		endgame = game.process_events()
		game.run_logic()
		game.display_frame(screen)
		ball.update(screen)
		# screeball.update(screen)n.fill((0,0,0))
		pg.display.update()
		clock.tick(10)
		
if __name__ == "__main__":
	main()	