#Создание контекстного меню
from tkinter import *

x = 0
y = 0

window = Tk()
c = Canvas(window,width=300,height=300,bg='white')
c.pack()

def popup(event):
    global x,y
    x = event.x
    y = event.y
    menu.post(event.x_root,event.y_root)
    

def circle():
    c.create_oval(x,y,x+30,y+30)

def square():
    c.create_rectangle(x,y,x+30,y+30)

c.bind('<Button-3>',popup)

menu = Menu(tearoff=0)
menu.add_command(label='Круг',command=circle)
menu.add_command(label='Квадрат',command=square)



window.mainloop()