
import turtle

t = turtle.Turtle() # Создать черепашку

t.screen.setup(800,800) # Создать экран 800 на 800 пикселей


t.begin_fill() # Начать заполнение 
t.fillcolor('red') #Цвет заполнения
for i in range(4):
	t.fd(100) # Движение вперед
	t.lt(90)
t.end_fill() # Закончить заполнение







t.screen.exitonclick() # Клик по экрану - закрыть программу 
t.screen.mainloop() # Главный цикл

