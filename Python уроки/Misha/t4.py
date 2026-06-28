#Домик
import turtle

Max = turtle.Turtle() # Создать черепашку

Max.screen.setup(800,800) # Создать экран 800 на 800 пикселей


for i in range(4):
	Max.rt(90)
	Max.fd(100) # Движение вперед
	
for i in range(3):
	Max.left(120)
	Max.forward(100) # Движение вперед
	
Max.lt(30)

Max.setheading(90)




Max.screen.exitonclick() # Клик по экрану - закрыть программу 
Max.screen.mainloop() # Главный цикл

