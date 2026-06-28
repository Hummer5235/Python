#Пробуем залить frames и разместить на них текст
import tkinter as tk

window = tk.Tk()

label1 = tk.Label(master=window,text='label1',bg='red',fg='white')
label1.pack()


frame1 = tk.Frame(master=window,bg = 'black')
frame1.pack()

label2 = tk.Label(master=frame1,text='Hello, it is label2 on frame 1',bg='blue',fg='white')
label2.pack()

label3 = tk.Label(master=frame1,text='It is label3 on frame 1',bg='blue',fg='white')
label3.pack()

frame2 = tk.Frame(master=window,width=350,height=150,bg = 'black')
frame2.pack()








window.mainloop()