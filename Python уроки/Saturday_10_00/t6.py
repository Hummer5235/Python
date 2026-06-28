import turtle

t = turtle.Turtle()

x = 800
y = 800

t.screen.setup(x,y) #Задать размеры окна
t.pensize(3) # Размер черепашки
t.speed(50)

width = 30


for j in range(300):
	for i in range(4):
		t.fd(width)
		t.lt(90)
	width += 2
	t.lt(5)

	





t.screen.exitonclick() 
t.screen.mainloop() # Вызов бесконечого цикла окна