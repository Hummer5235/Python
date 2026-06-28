import turtle

t = turtle.Turtle()

x = 800
y = 800

t.screen.setup(x,y) #Задать размеры окна

t.pensize(10) # Размер черепашки


# t.fd(300)  Движение вперед forward
# t.bk(300)  Движение назад back
# t.lt(90) Поворот налево left
# t.rt(90) Поворот направо right

width = 50

t.fd(width)
t.lt(90)
t.fd(width)
t.lt(90)
t.fd(width)
t.lt(90)
t.fd(width)

t.fd(width)
t.rt(90)
t.fd(width)
t.rt(90)
t.fd(width)
t.rt(90)
t.fd(width)

t.fd(width)
t.rt(90)
t.fd(width)
t.rt(90)
t.fd(width)
t.rt(90)
t.fd(width)

t.fd(width)
t.lt(90)
t.fd(width)
t.lt(90)
t.fd(width)
t.lt(90)
t.fd(width)

t.rt(90)
t.fd(150)





# t.screen.exitonclick() # Закрытие экрана ЛКМ
t.screen.mainloop() # Вызов бесконечого цикла окна