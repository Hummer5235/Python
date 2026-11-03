from  tkinter import *
from time import sleep

window = Tk()
window.title('Test')


def set_screen():
    # Устанавливаем размеры окна
    window_width = 350
    window_height = 250

    # Получение размеров экрана
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Вычисление координат
    x = screen_width // 2 - window_width // 2
    y = screen_height // 2 - window_height // 2

    window.geometry(f'{window_width}x{window_height}+{x}+{y}')  # Размеры и позиция

set_screen()


#Кнопки
btn = Button(text='Нажми на меня 2') # Кнопка из пакета tkinter
btn.pack()


from tkinter import ttk

btn2 = ttk.Button(text='Нажми на меня 2')
btn2.pack()

btn2.config(text='Не нажимай, остановись')


window.mainloop()


