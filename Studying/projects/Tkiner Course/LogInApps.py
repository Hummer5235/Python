from tkinter import *
from PIL import ImageTk,Image
from tkhtmlview import HTMLLabel
import webbrowser



window = Tk()
window.title('LogIn')
window.geometry('500x600')

#images
bg_image = Image.open('Icons/Background.jpg').resize((500, 600))
bg_image_copy = bg_image.copy()
bg_image = ImageTk.PhotoImage(bg_image)

login_image = Image.open('Icons/logInBtn.png').resize((300,80))
login_image = ImageTk.PhotoImage(login_image)

vk_image = Image.open('Icons/vk_logo2.jpg').resize((30,30))
vk_image= ImageTk.PhotoImage(vk_image)

ok_image = Image.open('Icons/ok_logo.png').resize((40,30))
ok_image= ImageTk.PhotoImage(ok_image)


def resize_image(event):

    image = bg_image_copy.resize((event.width,event.height))
    bg_image = ImageTk.PhotoImage(image)
    lbl.config(image=bg_image)
    lbl.place(relx=0,rely=0)


def callback_vk():
    webbrowser.open('https://vk.com')
def callback_ok():
    webbrowser.open('https://ok.ru')

def enter(event,win):
    win.delete(0, END)
    win.config(fg='black')

def replace_chars(event):
    print('Activate')
    words = pass_ent.get()
    lst = ['*' for i in words]
    lst+='*'
    res = ''.join(lst)
    pass_ent.delete(0,END)
    # pass_ent.insert(0,res)
    # print(res)


lbl = Label(image=bg_image)
lbl.pack(fill=BOTH,expand=1)

lbl_log = Label(text='Log in',font='Consolas 20',borderwidth=0)
lbl_log.place(relx=0.42,rely=0.1)

log_ent = Entry(width=30,fg='grey')
log_ent.insert(0,'Login')
log_ent.place(relx=0.25,rely=0.3)

pass_ent = Entry(width=30,fg='grey')
pass_ent.insert(0,'Password')
pass_ent.place(relx=0.25,rely=0.4)

vk_btn = Button(text='Vkontakte',image=vk_image,compound=LEFT,font='Consolas 15',command=callback_vk,width=200,height=30,bg='white')
vk_btn.place(relx=0.1,rely=0.7)


ok_btn = Button(text='Odnoklassniki',image=ok_image,compound=LEFT,font='Consolas 15',command=callback_ok,width=200,height=30,bg='white')
ok_btn.place(relx=0.53,rely=0.7)

#События при нажатии на окна ввода
log_ent.bind('<Button-1>',lambda event: enter(event,log_ent))
pass_ent.bind('<Button-1>',lambda event: enter(event,pass_ent))
# pass_ent.bind('<KeyPress>',replace_chars)
# lbl.bind('<Configure>',resize_image)


# login_btn = Button(text='LogIn',image=login_image,font='Consolas 15', bg='#ccc8fa',borderwidth=0)
login_btn = Button(text='LogIn',font='Consolas 15', bg='#ccc8fa',borderwidth=5,width=20,)
login_btn.place(relx=0.3,rely=0.5)



window.mainloop()