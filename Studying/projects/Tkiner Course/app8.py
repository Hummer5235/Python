#Метод bind и события
import tkinter as tk

window = tk.Tk()
window.rowconfigure(0,minsize=50)
window.columnconfigure((0,1,2),minsize=50)

def handle_keypress(event):
    print(event.char)

window.bind('<Key>',handle_keypress)

def plus():
    value = int(lbl['text'])
    lbl['text'] = str(value+1)

def minus():
    value = int(lbl['text'])
    lbl['text'] = str(value-1)

btn_minus = tk.Button(text='-',command=minus)
# btn_minus.pack(side='left')
btn_minus.grid(row=0,column=0,sticky='nsew')

lbl = tk.Label(text='0')
# lbl.pack(side='left')
lbl.grid(row=0,column=1)

btn_plus = tk.Button(text='+',command=plus)
# btn_plus.pack(side='left')
btn_plus.grid(row=0,column=2,sticky='nsew')


window.mainloop()