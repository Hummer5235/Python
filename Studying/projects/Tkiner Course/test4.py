from tkinter import *
from tkinter import messagebox

window = Tk()
window.title('Заголовок окна')
window.geometry('300x200+500+400')

#Создание доп окна
window_sub = Toplevel()
lbl2 = Label(window_sub,text='Жопа',font='Consolas 150 bold')
lbl2.pack()

#
window_sub2 = Menu()
window_sub2.add_command(label='Жопчик')
window.config(menu=window_sub2)


# messagebox.askyesnocancel('Заголовок messagebox','''Внимание, вы запустили программу, если ее так можно назвать.''')
messagebox.showwarning('Заголовок messagebox','''Внимание, вы запустили программу, если ее так можно назвать.''')


lbl = Label(text='Тестовый текст')
ent = Entry()
btn = Button(text='Click')




window.mainloop()