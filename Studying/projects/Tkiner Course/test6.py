from tkinter import *
from tkinter import ttk


window = Tk()
window.geometry('300x200')

lbl1 = Label(text='Купить хлеб')
lbl1.grid(row=0,column=0)

ch_btn = Checkbutton()
ch_btn.grid(row=0,column=1)

lbox = Listbox(width=15,height=8)
lbox.grid(row=2,column=0)

for i in ('one','two','three','four','five'):
    lbox.insert(1,i)

combox = ttk.Combobox(values=('one','two','three','four','five'))
combox.grid(row=3,column=0)


scl = Scale(orient='horizontal')
scl.grid(row=1,column=0)


window.mainloop()