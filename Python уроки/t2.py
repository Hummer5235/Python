import turtle

t = turtle.Turtle() #
W,H = 1000,1000
t.screen.setup(W,H) # Задать размер окна
# t.speed(100)
t.color("black")
t.pensize(2)

t.begin_fill()
for i in range (72):
    t.fd(20)
    t.dot(10,"yellow")
    t.lt(5)


t.fillcolor("red")
t.end_fill()






t.screen.exitonclick()
t.screen.mainloop()