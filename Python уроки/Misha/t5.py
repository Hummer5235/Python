#Круги

import turtle

t = turtle.Turtle() # Создать черепашку

t.screen.setup(800,800) # Создать экран 800 на 800 пикселей
t.hideturtle()
t.color('black')
t.screen.bgcolor('orange')
t.shape('classic')
t.pensize(10)
t.speed(5)


#t.circle(r,a)  r - радиус, a - часть окружности в градусах
t.circle(150, 360)

t.up()
t.goto(-50,220)
t.down()
#Левый глаз
t.circle(20,360)

t.up()
t.fd(100)
t.down()
#Правый глаз
t.circle(20,360)

t.up()
t.bk(50)
t.down()
t.rt(90)
t.fd(100)

t.up()

t.rt(90)
t.fd(75)	
t.lt(90)
t.fd(20)
t.rt(90)
t.lt(150)
t.down()
t.circle(150,60)



t.screen.exitonclick() # Клик по экрану - закрыть программу 
t.screen.mainloop() # Главный цикл

