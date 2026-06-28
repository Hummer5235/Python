
import turtle

t = turtle.Turtle() # Создать черепашку

t.screen.setup(800,800) # Создать экран 800 на 800 пикселей
t.pensize(7)

t.lt(180)
t.lt(90)
t.circle(-200,20)
t.circle(-100,160)





t.screen.exitonclick() # Клик по экрану - закрыть программу 
t.screen.mainloop() # Главный цикл

