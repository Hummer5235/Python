
import turtle

t = turtle.Turtle() # Создать черепашку

t.screen.setup(1000,900)

t.pensize(5)


#Переход к началу рисунка
t.up()
t.fd(150)
t.lt(90)
t.down()


#Рисуем голову

t.fd(100)
t.circle(200,180)













t.screen.exitonclick()
t.screen.mainloop() # Главный цикл