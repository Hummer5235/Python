# Цветок , мельница

import turtle

t = turtle.Turtle() # Создать черепашку

t.screen.setup(800,800) # Создать экран с размерами 800*800

t.speed(20)
t.pensize(5)


t.lt(45)
for g in range(6):
	storona_kv = 100
	
	for j in range(20):

		for i in range(4): #Квадрат
			t.fd(storona_kv)
			t.lt(90)
		storona_kv += 20
	t.lt(60)





t.screen.exitonclick()
t.screen.mainloop() # Главный цикл