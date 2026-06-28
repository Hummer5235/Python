#Виджет TopLevel. Дочерние окна
from random import *
from tkinter import*

window = Tk()
window.title('Тестовое приложение')
window.geometry('500x500')
number = 1

def open_win():
    global number
    win = Toplevel()
    win.geometry(f'350x200+{randint(0,1000)}+{randint(0,1000)}')
    win.title(f'Дочернее окно №{number}')
    number+=1
    # win.overrideredirect(True) # Скрытие верхней панели
    # win.grab_set() #Запрет изменения/закрытия основного окна, если есть дочернее
    lbl = Label(win,font ='Arial 15 bold',fg='brown',text='TopLevel')
    lbl.pack()
    # win.after(3000,win.destroy) # Асинхронная

btn = Button(text='Открыть',command= lambda : [open_win() for i in range(50)] ).place(anchor=CENTER,relx=0.5,rely=0.5)


window.mainloop()
