#Создание блокнота Ч1
from tkinter import *

window = Tk()
window.geometry('600x400')
window.config(bg='black')


frm1 = Frame(bg='purple')
frm1.pack(fill=BOTH,expand=1)

text_field = Text(frm1,
                  bg='black',
                  fg='lime',
                  padx=10,
                  pady=10,
                  wrap=WORD,
                  insertbackground='yellow',  # Цвет выделения текста
                  selectbackground='grey',  # Цвет курсора
                  spacing1=10,  #При начале
                  spacing2=3,  #При переходе на другую строку
                  spacing3=20,  #Расстояние при нажатии Enter
                  width=20
                  )

text_field.pack(expand=1, fill=BOTH,side=LEFT)

scroll = Scrollbar(frm1,command=text_field.yview)
scroll.pack(side=LEFT,fill=Y)

text_field.config(yscrollcommand=scroll.set)


window.mainloop()