from tkinter import *
from PIL import Image,ImageTk


window = Tk()
window.geometry('500x350')
window.resizable(0,0)


frm1 = Frame()
frm1.pack()

bg_img = Image.open('Icons/bg_image.jpg').resize((500,500))
bg_img = ImageTk.PhotoImage(bg_img)



lbl_bg =Label(frm1,image=bg_img)
lbl_bg.grid(row=0,column=0)

lbl = Label(frm1,text='В начале было слово...')
lbl.place(relx=0,rely=0)

window.mainloop()