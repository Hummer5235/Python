import turtle 
t = turtle.Turtle() 
t.screen.setup(800,800) 
t.setheading(90)
t.speed(100)

# t.goto(x,y) - Перейти в точку с координатами
# t.setheading(90) - Установить угол поворота от начального положения
# t.dot(radius,color) - Точка 
# t.circle(radius,ф) - Радиус и часть окр (в градусах), которую рисуем t.circle(50,180)

# Круг с точками
t.up()
t.goto(350,0)
t.down()
t.fillcolor("cyan")
t.begin_fill()

for i in range(45):
	t.circle(350,360/45)
	t.dot(10,"yellow")
t.end_fill()

# Заливка цветом
t.begin_fill() # Начать заполнение, ставится перед началом рисования фигуры
t.end_fill() # Окончание заполнения - после рисунка



t.screen.exitonclick() 
t.screen.mainloop()
