import turtle,random


t = turtle.Turtle()
t.screen.setup(700,600)
colors = ["red","yellow","blue","green"]
t.speed(100)

l = 40
a = 90
for j in range(100):
	for i in range(4):
		t.fd(l)
		t.lt(a)
	t.lt(10)
	l+=3
	

t.screen.exitonclick() 
t.screen.mainloop()