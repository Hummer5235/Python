import turtle
t = turtle.Turtle()
x,y = 800,600
t.screen.setup(x,y)
t.speed(-1)
for i in range(72):
    for i in range(6):
        t.fd(100)
        t.lt(60)
    t.lt(5)



t.screen.mainloop()