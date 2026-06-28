#Рисование в tkinter. Класс Canvas
from tkinter import *


window = Tk()
window.title('Рисование')
window.geometry('800x600')
window.resizable(False,False)

canvas = Canvas(width=800,height=600,bg='white')
# canvas.create_rectangle(150,150,250,250,fill = 'lime',width=10)
# canvas.create_oval(150,150,450,250)

canvas.create_polygon(100,200,250,550,400,500,fill='#80CBC4',outline='black',width=2)
# canvas.create_polygon(150,250,250,350,350,450)
canvas.pack()




window.mainloop()