#Создание вкладок
from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry('400x250')
window.resizable(0,0)

# создаем набор вкладок
tab_control = ttk.Notebook()

tab1= ttk.Frame(tab_control)
tab2= ttk.Frame(tab_control)

tab_control.add(tab1,text='Первая')
tab_control.add(tab2,text='Вторая')

lbl1 = Label(tab1,text='Вкладка 1')
lbl1.grid(row=0,column=0)

lbl2 = Label(tab2,text='Вкладка 2')
lbl2.grid(row=0,column=0)
print(tab_control.tabs())

tab_control.pack(expand=1,fill=BOTH)

window.mainloop()