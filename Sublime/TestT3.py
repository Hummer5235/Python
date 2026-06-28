import turtle 
import random
t = turtle.Turtle()
t.hideturtle()
t.setheading(90)
t.shape("classic")
t.shapesize(1)


# Написание текста
# t.write(text, move, align, font = (fontname, fontsize, fontstyle))

t.write("Hello everyone!",False,"center",font=("Consolas",20,"normal"))
t.up()

# t.shape("circle") - Вид черепашки "arrow", "circle", "square", "triangle", "turtle", "classic"
# t.shapesize(1) - Размер черепашки

# t.hideturtle() - Спрятать черепашку
# t.showturtle() - ПОказать черепашку

for i in range(100):

	x=random.randint(-400,400)
	y=random.randint(-400,400)
	t.setpos(x,y)
	t.write("Hello everyone!",False,"center",font=("Consolas",20,"normal"))
t.showturtle()



t.screen.exitonclick() 
t.screen.mainloop()
