import tkinter as tk

window = tk.Tk()
window.title('Тестовое приложение')
window.iconbitmap('Icons/utilitiesterminalicon.ico')
window.resizable(width=False,height=False)


ent = tk.Entry(width=40)
ent.pack()

ent.insert(0,'What is your name?')

window.mainloop()