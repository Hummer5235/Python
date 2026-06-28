import pygame
from pygame.locals import *

BALLSPEED=10

class Ball(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((15,15))
		self.image.fill((255, 255, 0))
		self.rect = self.image.get_rect(center=(400,300))
		self.speedx = BALLSPEED 
		self.speedy = BALLSPEED *-1

	def update(self, keys, platform, *args):

		self.rect.y += self.speedy

		hitGroup = pygame.sprite.Group(platform)

		spriteHitList = pygame.sprite.spritecollide(self, hitGroup, False)

		if len(spriteHitList) > 0:
			self.speedy *= -1
			self.rect.y += self.speedy

		self.rect.x += self.speedx

		if self.rect.right > 800:
			self.speedx *= -1
			self.rect.right = 800

		if self.rect.left < 0:
			self.speedx *= -1
			self.rect.left = 0

		if self.rect.top < 0:
			self.speedy *= -1
			self.rect.top = 0




class Platform(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((60,10))
		self.rect = self.image.get_rect(center=(400,500))
		self.image.fill((255, 0, 0))

	def update(self,keys,*args):
		if keys[K_a] and self.rect.left > 0:
			self.rect.x -= 15
		if keys[K_d] and self.rect.right < 800 :
			self.rect.x += 15



class Game:
	def __init__(self):
		self.score=0
		self.game_over=0
		self.sprites=pygame.sprite.Group()
		self.platform=Platform()
		self.sprites.add(self.platform)
		ball=Ball()
		self.sprites.add(ball)

	def process_events(self):
		for event in pygame.event.get():
			if event.type==QUIT:
				return True
			if event.type==MOUSEBUTTONDOWN:
				if self.game_over==True:
					self.__init__()

	def run_logic(self):
		pass

	def display_frame(self,screen,keys):
		screen.fill((0,0,0))
		self.sprites.update(keys, self.platform)
		self.sprites.draw(screen)



def main():
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Plank")

    game=Game()
    endgame=False
    clock=pygame.time.Clock()

    while not endgame:
    	endgame=game.process_events()
    	game.run_logic()
    	keys=pygame.key.get_pressed()
    	game.display_frame(screen,keys)

    	pygame.display.update()
    	clock.tick(60)

main()
