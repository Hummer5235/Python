#Треугольник
import turtle

Max = turtle.Turtle() # Создать черепашку

Max.screen.setup(800,800) # Создать экран 800 на 800 пикселей



for i in range(3):
	Max.forward(100) # Движение вперед
	Max.left(120)

	





Max.screen.exitonclick() # Клик по экрану - закрыть программу 
Max.screen.mainloop() # Главный цикл

