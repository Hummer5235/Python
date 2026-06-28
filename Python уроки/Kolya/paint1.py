import turtle # Импортировать библиотеку
from  time import sleep

turtle.width(3)
turtle.begin_fill() # Начать закрашивать


sleep(3)
#Команды движения
turtle.up() # Подними перо
turtle.goto(-150,200) # Перейди в координаты
turtle.down() # Опусти перо


turtle.forward(100) # вперед
turtle.right(90) # поворот
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.end_fill() # Закончить закрашивать



turtle.exitonclick()
# turtle.mainloop() #Главный цикл