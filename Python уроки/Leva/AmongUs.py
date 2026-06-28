import turtle

t = turtle.Turtle()
x,y= 800,600
t.screen.setup(x,y)
t.screen.bgcolor("orange")
t.pensize(10)		

t.up()
t.goto(200,-200)
t.down()
t.lt(90)
t.fd(170)
t.rt(90)
t.fd(20)
t.circle(30,90)
# t.circle(100,180)




t.screen.mainloop()