#5 Снежинок

import turtle

t = turtle.Turtle() # Создать черепашку

t.screen.setup(1000,900) # Создать экран с размерами 800*800

t.speed(20)
t.pensize(2)
t.screen.bgcolor('black')
t.pencolor('blue')

t.up()
t.goto(-300,300)
t.down()

for g in range(12):
	storona_kv = 10
	
	for j in range(20):

		for i in range(4): #Квадрат
			t.fd(storona_kv)
			t.lt(90)
		storona_kv += 5
	t.lt(30)


t.up()
t.goto(300,-300)
t.down()


for g in range(12):
	storona_kv = 10
	
	for j in range(20):

		for i in range(4): #Квадрат
			t.fd(storona_kv)
			t.lt(90)
		storona_kv += 5
	t.lt(30)


t.up()
t.goto(-300,-300)
t.down()


for g in range(12):
	storona_kv = 10
	
	for j in range(20):

		for i in range(4): #Квадрат
			t.fd(storona_kv)
			t.lt(90)
		storona_kv += 5
	t.lt(30)

t.up()
t.goto(300,300)
t.down()


for g in range(12):
	storona_kv = 10
	
	for j in range(20):

		for i in range(4): #Квадрат
			t.fd(storona_kv)
			t.lt(90)
		storona_kv += 5
	t.lt(30)



t.up()
t.goto(0,0)
t.down()


for g in range(12):
	storona_kv = 10
	
	for j in range(20):

		for i in range(4): #Квадрат
			t.fd(storona_kv)
			t.lt(90)
		storona_kv += 5
	t.lt(30)


t.screen.exitonclick()
t.screen.mainloop() # Главный цикл