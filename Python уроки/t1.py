import turtle

t = turtle.Turtle() #
W,H = 1000,1000
t.screen.setup(W,H) # Задать размер окна
# t.speed(100)
t.screen.bgcolor("orange")
t.color("black")
t.pensize(2)
for i in range(120):
    for i in range(4):
        t.fd(200)
        t.lt(90)
    t.lt(3)






t.screen.exitonclick()
t.screen.mainloop()