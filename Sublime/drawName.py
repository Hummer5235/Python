import turtle # Импортируем модуль
import time

#t.up() - Поднять перо
#t.down() - Опустить перо
#t.goto(x,y) / t.setpos(x,y) / t.setposition(x,y)

t = turtle.Turtle() # Подключаем черепашку

t.screen.setup(950,650) # Размер экрана
t.speed(3) #Скорость черепашки
# Постановка на место

t.color("red")
t.pensize(10) # - Размер ручки
time.sleep(1)
t.up()
t
t.left(180)
t.fd(300)
t.rt(90)
t.fd(300)
t.rt(90)

# Буква "З"
for i in range(2):
	t.down()
	t.fd(100)
	t.rt(90)
	t.fd(100)
	t.rt(90)
	t.fd(100)
	t.up()
	t.rt(180)

t.fd(150)

# Буква "А""
t.lt(75)
for i in range(2):
	t.down()
	t.fd(210)
	t.rt(150)
t.up()	
t.rt(30)
t.fd(70)
t.lt(75)
t.down()
t.fd(73)
t.up()
t.lt(90)
t.fd(67)

t.lt(90)
t.fd(140)

# Буква "Х""
t.down()
t.lt(70)
t.fd(220)
t.up()
t.rt(180)
t.fd(110)
t.rt(133)
t.fd(110)
t.down()
t.lt(180)
t.fd(223)
t.lt(63)
t.up()
t.fd(50)

# Буква "А""
t.lt(75)
for i in range(2):
	t.down()
	t.fd(210)
	t.rt(150)
t.up()	
t.rt(30)
t.fd(70)
t.lt(75)
t.down()
t.fd(73)
t.up()
t.lt(90)
t.fd(67)

t.lt(90)
t.fd(140)

#Буква "Р"
t.down()
t.lt(90)
t.fd(200)
for i in range(3):
	t.rt(90)
	t.fd(85)

t.up()
t.lt(90)
t.fd(115)
t.lt(90)
t.fd(100)

#Точка
c = 90
l = 15
t.down()
t.lt(90)
for i in range(90):
	l-=0.16
	for i in range(4):
		t.fd(l)
		t.rt(c)
	c+=1




t.screen.exitonclick() # Выход на клик мышки
