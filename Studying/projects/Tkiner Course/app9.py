#Бросить кубик
import tkinter as tk
import random, time

window = tk.Tk()

window.columnconfigure(0,minsize=100)
window.rowconfigure((0,1),minsize=100)
img = 0

def animate_cube(number):
    global img
    img = tk.PhotoImage(file=f'Icons/Cube/{number}.png')
    label_img = tk.Label(image=img)
    label_img.grid(row=2, column=0)


def generate_number():
    number = random.randint(1,6)
    # value = int(lbl['text'])
    lbl['text'] = str(number)
    animate_cube(number)



btn =  tk.Button(text='Бросить кубик',
                 command=generate_number,
                 bg='#a10d77',
                 fg='white',
                 relief=tk.RAISED,
                 borderwidth=5,
                 activebackground='#fa25be',
                 font='Consolas 20 bold')

btn.grid(row=0,column=0,sticky='nswe')

lbl = tk.Label(text='0',
               bg='black',
               fg='white',
               relief=tk.RAISED,
               borderwidth=5,
               font='Consolas 20 bold')
lbl.grid(row=1,column=0,sticky='nswe')
animate_cube(6)



window.mainloop()