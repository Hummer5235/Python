#Кнопки
from tkinter import *

window = Tk()
# window.geometry('600x400')
# window.resizable(width=False,height=False)
window.iconbitmap('../Icons/utilitiesterminalicon.ico')
window.config(bg='black')

def click():
    print('Привет')

lst = [SUNKEN,RAISED,GROOVE,RIDGE]
for i in range(4):
    lbl = Label(window,
                 text='Кнопка',
                 font='Consolas 20 bold',
                 background='pink', # Фон кнопки
                 activebackground='green',
                 activeforeground='white',
                 relief=lst[i],
                 borderwidth=5
                 )
    lbl.pack()

img = PhotoImage(file='Screenshot_17.png')
label = Label(window,image=img)
label.pack()

window.mainloop()