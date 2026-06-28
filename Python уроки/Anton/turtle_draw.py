import turtle


t = turtle.Turtle()


t.screen.setup(800, 800)

t.shape('square')
t.pensize(5)

window = turtle.Screen()



def move_Up():
	x = t.position()[0]
	y = t.position()[1]
	t.setposition(x, y + 5)
	print(f"X равен: {x}")
	print(f"Y равен: {y}")


def move_down():
	x, y = t.position()
	t.setposition(x, y - 5)


def move_left():
	x, y = t.position()
	t.setposition(x - 5, y)



def move_right():
	x, y = t.position()
	t.setposition(x + 5, y)

def Up():
	t.up()

def down():
	t.down()

def clear():
	t.pencolor('white')



window.onkeypress(move_Up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(move_left, "a")
window.onkeypress(move_right, "d")
window.onkeypress(clear, "c")


window.onkey(Up, "x")
window.onkey(down, "z")


window.listen()

t.screen.mainloop()