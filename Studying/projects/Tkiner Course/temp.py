import tkinter as tk

window = tk.Tk()

label1 = tk.Label(text='Python')
label1.grid(row=0,sticky='we')
label2 = tk.Label(text = 'Введите свое имя: ')
label2.grid(row=1,column=0)

ent = tk.Entry()
ent.grid(row=1,column=1)



window.mainloop()