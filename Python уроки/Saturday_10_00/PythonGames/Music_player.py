import pygame
pygame.init()

W,H = 600, 400


#pygame.mixer - Для звуковых эффектов
#pygame.mixer.music - Для добавленяи музыки
volume = 0.1
d1 = pygame.mixer.music.load('Music/Music1_Deep.mp3') #Загрузить музыку
# d2 = pygame.mixer.music.load('Music/Music2_Deep.mp3') #Загрузить музыку

pygame.mixer.music.queue('Music/Music2_Deep.mp3')
pygame.mixer.music.play() #Запустить музыку
pygame.mixer.music.set_volume(volume)



screen = pygame.display.set_mode((600,400))
pygame.display.set_caption('Музыка')

Play = True


сlock = pygame.time.Clock()

while Play:
	for event in pygame.event.get():
		if event.type== pygame.KEYUP:
			if event.key== pygame.K_MINUS:
				print('---')
				volume -= 0.1
				pygame.mixer.music.set_volume(volume)
			elif event.key == pygame.K_EQUALS or pygame.K_KP_PLUS:
				print('+++')
				volume += 0.1
				pygame.mixer.music.set_volume(volume)
			elif event.key == pygame.K_LEFT:
				pass
		if event.type == pygame.QUIT:
			Play = False



	сlock.tick(60)

