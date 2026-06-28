#Секундомер

from tkinter import *
import datetime



window = Tk()
# window.geometry('300x230')
window.resizable(width=False,height=False)
window.title('Секундомер')
# window.rowconfigure(0,minsize=120)
# window.columnconfigure((0,1,2,3,4),minsize=120)

start_time = 0
activate = True
after_id = ''
def stopwatch():
    start_btn.pack_forget()
    stop_btn.pack()
    global start_time, activate, after_id

    real_time = datetime.datetime.fromtimestamp(start_time).strftime('%M:%S')
    start_time+=1
    after_id = window.after(1000,stopwatch) # Рекурсивная функция
    lbl['text'] = str(real_time)


def stop_time():
    stop_btn.pack_forget()
    continue_btn.pack()
    reset_btn.pack()
    window.after_cancel(after_id)

def continue_time():
    continue_btn.pack_forget()
    reset_btn.pack_forget()
    stopwatch()

def reset_time():
    global start_time
    start_time = 0
    lbl['text'] = '00:00'
    continue_btn.pack_forget()
    reset_btn.pack_forget()
    start_btn.pack()


lbl = Label(text='00:00',font='Consolas 30')
lbl.pack()

start_btn = Button(text='Start',
                   font='Consolas 30',
                   bg='#d45757',
                   fg='white',
                   activebackground='black',
                   activeforeground='white',
                   relief=RAISED,
                   borderwidth=5,
                   width=15,
                   command=stopwatch)
start_btn.pack()

stop_btn = Button(text='Stop',
                   font='Consolas 30',
                   bg='#d45757',
                   fg='white',
                   activebackground='black',
                   activeforeground='white',
                   relief=RAISED,
                   borderwidth=5,
                   width=15,
                   command=stop_time)

continue_btn = Button(text='Continue',
                   font='Consolas 30',
                   bg='#d45757',
                   fg='white',
                   activebackground='black',
                   activeforeground='white',
                   relief=RAISED,
                   borderwidth=5,
                   width=15,
                   command=continue_time)



reset_btn = Button(text='Reset',
                   font='Consolas 30',
                   bg='#d45757',
                   fg='white',
                   activebackground='black',
                   activeforeground='white',
                   relief=RAISED,
                   borderwidth=5,
                   width=15,
                   command=reset_time)




window.mainloop()