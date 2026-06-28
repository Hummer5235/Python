import turtle 
import random
import time 

t = turtle.Turtle() 
t.screen.bgcolor("orange") # Цвет заднего фона
t.screen.setup(700,600)
t.up()
t.setpos(-100,-200)
t.down()


t.shape("turtle")
t.color("blue")
t.stamp() # След черепашки, штамп
t.color("black")
t.up()
t.fd(50)
t.down()
t.circle(200, 70)



t.pensize(10) # Установить ширину линии

t.color("blue")
t.stamp()
t.color("black")
t.up()
t.fd(50)
t.down()
t.circle(200, 70)

t.clear() # Очистить экран
time.sleep(3)

t.color("blue")
t.stamp()
t.color("black")
t.up()
t.fd(50)
t.down()
t.circle(200, 70)

time.sleep(3)
t.reset() # Очистить экран и поставить в центр

t.screen.exitonclick()
t.screen.mainloop()