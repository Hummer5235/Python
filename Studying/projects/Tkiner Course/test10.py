#Знакомство с Canvas
from tkinter import *


window = Tk()
window.title('Работа с Canvas')
window.geometry('400x400')

c = Canvas(width=400,height=400,bg='white')
c.pack()

roof = c.create_polygon(150,250,320,250,235,170,fill='lightblue')
walls = c.create_rectangle(170,250,300,350,fill='lightblue',outline='lightblue')
sun = c.create_oval(330,10,380,60,fill='orange',outline='orange')


for x in range(-1,20):
    grass = c.create_arc(x*20,470,90+x*20,350,style = ARC,
                        start = 180,extent = -70,outline='green',width=3)

window.mainloop()