#Метод pack
from tkinter import *

window = Tk()
window.title('Тестовое приложение')
window.geometry('600x400')
window.resizable(width=False,height=False)
window.config(bg='black')


l1 = Label(text='1', font='15',fg='black',bg='yellow',width=8,height=4).pack(side=LEFT)
l2 = Label(text='2', font='15',fg='black',bg='brown',width=8,height=4).pack(side=RIGHT)
l3 = Label(text='3', font='15',fg='black',bg='blue',width=8,height=4).pack(side=TOP)
l4 = Label(text='4', font='15',fg='black',bg='white',width=8,height=4).pack(side=BOTTOM)




window.mainloop()