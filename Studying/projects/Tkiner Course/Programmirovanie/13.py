#Создание блокнота Ч3 Изменение тем, шрифта, выход, messagebox
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename,asksaveasfilename


window = Tk()
window.geometry('600x400')
window.config(bg='black')




def change_theme(style):
    global view_colors
    color_scheme = view_colors[style]
    text_field['bg']=color_scheme['text_bg']
    text_field['fg']=color_scheme['text_fg']
    text_field['insertbackground']=color_scheme['cursor']
    text_field['selectbackground']=color_scheme['select_bg']

def change_font(font_style):
    text_field['font']=fonts[font_style]

def notepad_exit():
    # answer = messagebox.askyesno('Выход','Закрыть приложение?')
    answer = messagebox.askokcancel('Выход','Вы точно хотите выйти?')
    print(answer)
    if answer:
        window.destroy()


def open_file():
    #Открывает файл для редактирования
    filepath = askopenfilename(filetypes=[('Text Files','*.txt'),('All Files','*.*')])
    if not filepath:
        return None
    text_field.delete('1.0',END)
    with open(filepath,'r',encoding='utf-8') as input_file:
        text = input_file.read()
        text_field.insert(END,text)
    window.title(f'Простой текстовый редактор {filepath}')
#
def save_file():
    filepath = asksaveasfilename(
        defaultextension='txt',
        filetypes=[('Текстовые файлы','*.txt'),('Все файлы','*.*')])
    if not filepath:
        return None
    with open(filepath,'w',encoding='utf-8') as output_file:
        text = text_field.get('1.0',END)
        output_file.write(text)
    window.title(f'Простой текстовый редактор {filepath}')

main_menu = Menu()#Создание экземпляра меню для добавления строк

#----------------------------Файл---------------------------------------
file_menu = Menu(tearoff=False) #Создание подменю для кнопки Файл
file_menu.add_command(label='Открыть',command=open_file)
file_menu.add_command(label='Сохранить',command=save_file)
file_menu.add_separator()
file_menu.add_command(label='Закрыть',command=notepad_exit)
main_menu.add_cascade(label='Файл',menu=file_menu)#Добавление подменю в основное меню


#----------------------------Вид---------------------------------------
view_menu = Menu(tearoff=False)#Создание подменю для кнопки Вид
view_menu.add_command(label='Флажки элементов')
view_menu.add_command(label='Расширения имен файлов')
view_menu.add_command(label='Скрытые элементы')

view_menu_theme = Menu(tearoff=False)
view_menu_theme.add_command(label='Темная',command=lambda : change_theme('dark'))
view_menu_theme.add_command(label='Светлая',command=lambda : change_theme('light'))

view_menu_font = Menu(tearoff=False)
view_menu_font.add_command(label='Arial', command= lambda : change_font('Arial'))
view_menu_font.add_command(label='Comic Sans MS', command= lambda : change_font('Comic Sans MS'))
view_menu_font.add_command(label='Consolas', command= lambda : change_font('Consolas'))


main_menu.add_cascade(label='Вид',menu=view_menu)
view_menu.add_cascade(label='Тема',menu=view_menu_theme)
view_menu.add_cascade(label='Шрифт',menu=view_menu_font)
window.config(menu=main_menu)


frm1 = Frame(bg='purple')
frm1.pack(fill=BOTH,expand=1)

view_colors = {
    'dark':{'text_bg':'black','text_fg':'lime','cursor':'grey','select_bg':'yellow'},
    'light':{'text_bg':'white','text_fg':'black','cursor':'grey','select_bg':'#5269d9'},
}

fonts= {'Comic Sans MS':('Comic Sans MS',),'Arial':'Arial',
        'Consolas':'Consolas'
}

text_field = Text(frm1,
                  bg='black',
                  fg='lime',
                  padx=10,
                  pady=10,
                  wrap=WORD,
                  insertbackground='yellow',#Цвет выделения текста
                  selectbackground='grey', #Цвет курсора
                  spacing1=10,#При начале
                  spacing2=3,#При переходе на другую строку
                  spacing3=20,#Расстояние при нажатии Enter
                  width=20,
                  )

text_field.pack(expand=1, fill=BOTH,side=LEFT)

scroll = Scrollbar(frm1,command=text_field.yview)
scroll.pack(side=LEFT,fill=Y)

text_field.config(yscrollcommand=scroll.set)


window.mainloop()