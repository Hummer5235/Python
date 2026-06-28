import turtle

t = turtle.Turtle()
turtle.Screen()
t.speed(0)
t.up()
t.pensize(5)
t.hideturtle()
t.color("red")
t.goto(-200,200)
t.down()
t.goto(200,200)
t.goto(200,-200)
t.goto(-200,-200)
t.goto(-200,200)

ball=turtle.Turtle()
ball.shape("circle")

while True:
	x,y = ball.position()

	ball.goto(x+1,y)
	



turtle.exitonclick()