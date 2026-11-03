from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Buttons test')
root.geometry("350x200")

clicks = 0

def click_button():
    global clicks
    clicks +=1
    print('Клик!')
    btn.config(text=f'Clicks: {clicks}')

#Обработка нажатия на кнопку ,параметр command
btn = ttk.Button(text='Button',command=click_button)
#Отключение кнопки с помощью параметра state
btn2 = ttk.Button(text='Button2',command=click_button,state=['disabled'])

btn.pack()
btn2.pack()

root.mainloop()
