#Tkinter - интерфейс в Python ля графич. библиотеки Tk


from tkinter import *

window = Tk() # Создаем объект - окно
window.title('Мини окно') # Заголовок окна
icon = PhotoImage(file='picture.png')
window.iconbitmap(False,icon)

#Устанавливаем размеры окна
window_width = 500
window_height = 550



#Получение размеров экрана
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

#Вычисление координат
x = screen_width//2 - window_width//2
y = screen_height//2 - window_height//2

window.geometry(f'{window_width}x{window_height}+{x}+{y}') #Размеры и позиция





print(window_width,window_height)


#Виджеты - элементы внутри окна
label = Label(text='Добрый день, дорогой пользователь')

#Для размещения объекта в окне используем метод pack
label.pack()






window.mainloop() #запускаем главный цикл обработки событий