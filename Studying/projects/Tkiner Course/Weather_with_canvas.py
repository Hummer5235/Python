from tkinter import *
from PIL import ImageTk,Image
import sys
sys.path.insert(0, '/Studying/projects/Network/HubStudio')
from file2 import get_weather


window = Tk()
W,H = 500,600
window.geometry(f'{W}x{H}')
# window.resizable(False,False)
window.title('Текущая погода')
color = 'lightblue'

img = Image.open('Icons/Village_bg2.jpg')
img = ImageTk.PhotoImage(img)

# bg = Label(image=img)
# bg.place(relx=0.5,rely=0.4,anchor=CENTER)


canv1 = Canvas()
canv1.create_image(-500,-100,image=img,anchor = NW)
canv1.create_text(255,160,text='Погода',font='Consolas 25 bold')
# screen = canv1.create_text(270,330,text='',font='Consolas 15 bold')
screen = Label(canv1,text='',font='Consolas 13 bold',bg=color)

# canv1.place(relx=0.3,rely=0.2)
canv1.pack(fill=BOTH,expand=1)

# lbl = Label(text='Погода',font='Consolas 25 bold',bg=color)
# lbl.place(relx=0.5,rely=0.1,anchor=CENTER)

ent = Entry(foreground='grey')
ent.place(relx=0.5,rely=0.35,anchor=CENTER)
ent.insert(0,'Введите город')



def choose_entry(event):
    ent.delete(0,END)
    ent.config(foreground='black',font='Consolas 13 bold')


def check_weather(event= None):

    city = ent.get()
    if len(get_weather(city))==2:
        weather, temp = get_weather(city)
        # print(weather.py)
        screen.config(text=f'{weather}\n{temp}')
    else:
        answer = get_weather(city)
        screen.config(text=f'{answer}')
    screen.place(relx=0.5, rely=0.5, anchor=CENTER)




btn = Button(text='Узнать погоду',font='Consolas 15 bold',bg=color,relief=RAISED,borderwidth=5,
             command=check_weather)
btn.place(relx=0.5,rely=0.7,anchor=CENTER)
ent.bind('<Button-1>',choose_entry)
ent.bind('<Return>',check_weather)



window.mainloop()