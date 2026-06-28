from tkinter import *
from PIL import ImageTk,Image



window = Tk()
window.geometry('800x600')
window.title('Работа с Canvas')


canvas = Canvas(bg='white')



login_image = Image.open('Icons/logInBtn.png').resize((300,50))
login_image = ImageTk.PhotoImage(login_image)

img = Image.open('Icons/nastol.com.ua-281233.jpg').resize((800,600))
img = ImageTk.PhotoImage(img)
canvas.create_image(10,10,anchor=NW,image=img)


btn1 = Button(canvas,text='Click!',image=login_image,borderwidth=0,bg='white',activebackground='white')
btn1.pack(side=BOTTOM)

# canvas.create_rectangle(100,100,400,200,fill='red',dash=(1,2))
canvas.create_text(350,350,text='Tkinter!',font='Consolas 20',fill='Yellow',activefill='red')
canvas.pack(fill=BOTH,expand=1)



window.mainloop()