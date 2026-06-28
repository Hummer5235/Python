import turtle 
import random
import time 

t = turtle.Turtle() 
t.screen.bgcolor("orange") # Цвет заднего фона
t.pensize(5)
t.speed(0)
# for i in range(100):
# 	t.fd(150)
# 	t.rt(110)

for i in range(36):
	t.down()
	t.fd(100)
	t.rt(20)
	t.fd(50)
	t.lt(30)
	t.fd(50)
	t.up()
	t.goto(0,0)


turtle.done()
