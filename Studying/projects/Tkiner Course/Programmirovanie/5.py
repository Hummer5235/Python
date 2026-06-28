#Счетчик кликов
from tkinter import *
from random import *

window = Tk()
window.geometry('600x400')
window.title('Счетчик кликов')
window.config(bg='black')
window.resizable(width=False,height=False)

def click():
    value = int(lbl['text'])
    value += 1
    lbl['text'] = str(value)
    btn.place(x = randint(50,550),y= randint(50,350))



lbl = Label(text='0',bg='black',foreground='white',font='Consolas 30')
lbl.place(x=300,y=110)

btn = Button(text='Click',font='Consolas 20',bg='green',command=click)
btn.place(x=260,y=180)









window.mainloop()