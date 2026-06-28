import turtle


step = 10
turtle.width(3)


for j in range(50):
    for i in range(4):
        turtle.fd(step)
        turtle.rt(90)
    step= step+10

turtle.exitonclick()