import turtle
t = turtle.Turtle()
t.speed(5)
t.pensize(5)
t.screen.bgcolor("orange")
t.up()
t.goto(0,200)
t.down()
t.circle(100,360)
t.up()
t.rt(90)
t.fd(240)
t.lt(90)
t.down()
t.circle(120,360)
t.up()
t.rt(90)
t.fd(280)
t.lt(90)
t.down()
t.circle(140,360)
t.up()
t.lt(90)

for i in range(2):
	for i in range(3):
		t.fd(70)
		t.dot(10,"yellow")
	t.fd(80)

t.fd(30)
t.dot(15,"red")
t.fd(10)
t.rt(90)
t.fd(70)
t.dot(20,"black")
t.lt(180)
t.fd(140)
t.dot(20,"black")
t.hideturtle()









t.screen.exitonclick() 
t.screen.mainloop()
