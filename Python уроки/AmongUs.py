import turtle

t = turtle.Turtle() #
W,H = 1000,1000
t.screen.setup(W,H) # Задать размер окна
# t.speed(100)
t.pensize(20)

BODY_COLOR = "red"
GLASS_COLOR = "blue"

t.color("black")
t.hideturtle()
t.penup()
t.goto(250,0)
t.pendown()
t.showturtle()


t.begin_fill()
t.lt(90)
t.fd(100)

t.circle(200,180)
t.rt(90)
t.fd(70)
t.fillcolor("red")
t.end_fill()
# Портфель
t.fillcolor('blue')
t.begin_fill()
t.circle(50,90)
t.fd(150)
t.circle(50,90)
t.fd(70)
t.lt(90)
t.fd(250)
t.end_fill()
t.fillcolor("red")
t.begin_fill()
t.lt(180)
t.fd(250)
# Ноги
t.fd(100)
t.circle(70,180)
t.fd(70)
t.rt(90)
t.fd(120)
t.rt(90)
t.fd(70)
t.circle(70,180)
t.fd(250)
t.fillcolor("red")
t.end_fill()

#Очки
t.rt(90)
t.begin_fill()
t.circle(70,180)
t.fd(300)
t.lt(90)
t.fd(140)
t.lt(90)
t.fd(300)
t.fillcolor("skyblue")
t.end_fill()









t.screen.exitonclick()
t.screen.mainloop()