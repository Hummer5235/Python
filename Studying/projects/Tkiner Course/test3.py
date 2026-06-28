#9 кнопок
from tkinter import *
import datetime

window = Tk()
window.geometry('277x277+450+270')
window.title('Тестовое окно')

buttons_list = []

frame1 = Frame(bg='black')
frame1.pack(expand=1,fill=BOTH)

number_of_button = 1

def time(btn):
    print(btn)
    real_time = datetime.datetime.now().time().strftime('%H:%M:%S')
    buttons_list[0].config(text=real_time)


def create_buttons():
    global number_of_button
    for i in range(3):
        for j in range(3):
            btn = Button(frame1,text=f'Button{number_of_button}',
                         bg='yellow',
                         font='Consolas',
                         width=7,
                         height=3,
                         activebackground='black',
                         activeforeground='white',
                         relief=RAISED,
                         borderwidth=5,
                         command=lambda : time(btn),

                         )
            buttons_list.append(btn)
            number_of_button+=1
            btn.grid(row=i,column=j)


create_buttons()

window.mainloop()