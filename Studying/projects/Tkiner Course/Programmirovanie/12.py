#Создание блокнота Ч2 Меню
from tkinter import *

window = Tk()
window.geometry('600x400')
window.config(bg='black')

main_menu = Menu()#Создание экземпляра меню для добавления строк

#----------------------------Файл---------------------------------------
file_menu = Menu(tearoff=False) #Создание подменю для кнопки Файл
file_menu.add_command(label='Открыть')
file_menu.add_command(label='Сохранить')
file_menu.add_separator()
file_menu.add_command(label='Закрыть')
main_menu.add_cascade(label='Файл',menu=file_menu)#Добавление подменю в основное меню


#----------------------------Вид---------------------------------------
view_menu = Menu(tearoff=False)#Создание подменю для кнопки Вид
view_menu.add_command(label='Флажки элементов')
view_menu.add_command(label='Расширения имен файлов')
view_menu.add_command(label='Скрытые элементы')

view_menu_theme = Menu(tearoff=False)
view_menu_theme.add_command(label='Темная')
view_menu_theme.add_command(label='Светлая')

view_menu_font = Menu(tearoff=False)
view_menu_font.add_command(label='Arial')
view_menu_font.add_command(label='Comic Sans MS')
view_menu_font.add_command(label='Consolas')


main_menu.add_cascade(label='Вид',menu=view_menu)
view_menu.add_cascade(label='Тема',menu=view_menu_theme)
view_menu.add_cascade(label='Шрифт',menu=view_menu_font)
window.config(menu=main_menu)


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