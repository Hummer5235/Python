#Кнопки
from tkinter import *

window = Tk()
window.geometry('600x400')
window.resizable(width=False,height=False)
window.iconbitmap('../Icons/utilitiesterminalicon.ico')
window.config(bg='black')

def click():
    print('Привет')

lst = [SUNKEN,RAISED,GROOVE,RIDGE]
for i in range(4):
    btn = Button(window,
                 text='Кнопка',
                 command=click,
                 font='Consolas 20',
                 background='pink', # Фон кнопки
                 activebackground='green',
                 activeforeground='white',
                 relief=lst[i],
                 borderwidth=5
                 )
    btn.pack()



window.mainloop()