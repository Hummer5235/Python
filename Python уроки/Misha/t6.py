#Квадрат
import turtle

Max = turtle.Turtle() # Создать черепашку

Max.screen.setup(800,800) # Создать экран 800 на 800 пикселей
Max.pensize(10)
Max.speed(5)
length = 150

for j in range(48):
	for i in range(4):
		Max.fd(length) # Движение вперед
		Max.lt(90)
	Max.lt(15)
	length = length+20








Max.screen.exitonclick() # Клик по экрану - закрыть программу 
Max.screen.mainloop() # Главный цикл

