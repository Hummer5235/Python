#Шуточная игра. Убегающая кнопка "Да"
from tkinter import *
from tkinter import messagebox
from random import *
from PIL import ImageTk, Image


window = Tk()
W,H=500,500
window.geometry(f'{W}x{H}')
window.title('Опрос')
window.resizable(False,False)
# window.config(bg='white')
# window.wm_attributes('-transparentcolor','grey')


bg_image = Image.open('bg_image2.jpg').resize((W,H))
bg_image = ImageTk.PhotoImage(bg_image)
bg_lbl = Label(image=bg_image)
bg_lbl.grid(row=0,column=0)

def no():
    messagebox.showinfo(title='Оповещение',message='Спасибо, Ваш голос учтен!')
    window.destroy()

def entered(event):
    x= randint(0,W-100)
    y= randint(0,H-100)
    btn_yes.place(x= x,y= y)

lbl = Label(text='Хотите ли вы увеличение зарплаты?',
            font='Consolas 15 '
            )
lbl.place(x=70,y=20)

btn_yes = Button(text='Да',
                 width=5,
                 relief=RAISED,
                 borderwidth=3,
                 font='Consolas 15 ')
btn_yes.place(x= 150,y=100)
btn_yes.bind('<Enter>',entered)

btn_no = Button(text='Нет',
                width=5,
                relief=RAISED,
                borderwidth=3,
                font='Consolas 15 bold',
                command=no)
btn_no.place(x= 300,y=100)


window.mainloop()