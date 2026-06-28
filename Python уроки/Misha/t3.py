#Пунктир
import turtle

Max = turtle.Turtle() # Создать черепашку

Max.screen.setup(800,800) # Создать экран 800 на 800 пикселей
Max.up()
Max.goto(-400,0)
Max.down()
for i in range(10):
	Max.fd(50) # Движение вперед
	Max.up()
	Max.fd(20)
	Max.down()
	







Max.screen.exitonclick() # Клик по экрану - закрыть программу 
Max.screen.mainloop() # Главный цикл

