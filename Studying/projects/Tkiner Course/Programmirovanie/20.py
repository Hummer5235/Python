#Добавление фона окна
from tkinter import *
from PIL import ImageTk,Image

window = Tk()
window.title('Фон окна')
W,H = 900,600
# window.resizable(False,False)
window.geometry(f'{W}x{H}')
# print(str(label.geometry()))

window_width = window.winfo_width()
window_height = window.winfo_height()

bg_image = Image.open('bg_image.jpg').resize((W,H))
bg_image =  ImageTk.PhotoImage(bg_image)
bg_lbl = Label(image=bg_image)
bg_lbl.grid(row=0,column=0)

btn = Button(text='Click',relief=RAISED, borderwidth=5,font=('Comic Sans MS',15))
btn.place(relx=0.5,rely=0.5)

window.mainloop()
