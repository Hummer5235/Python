# Урок 1
#1: Python файл, игровой цикл, дисплей
import pygame

pygame.init()

#Размеры экрана
display_width = 800
display_height = 600
display = pygame.display.set_mode((display_width,display_height)) # Установить размеры экрана
pygame.display.set_caption("Run Dino! Run!") # Установить название

icon = pygame.image.load("app_icon.png") # Загрузить изображение
pygame.display.set_icon(icon) # Установить иконку

def run_game():
    game = True

    while game:
        for event in pygame.event.get(): # Пройтись по всем событиям
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        display.fill((255,255,255))
        pygame.display.update() # Обновить дисплей


run_game()















