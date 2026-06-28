import tkinter as tk

window = tk.Tk()

frame1 = tk.Frame(master=window,width=350,height=150)
frame1.pack()

label1 = tk.Label(master=frame1,text='I am at(0,0)',bg='red',font='Consolas 20')
label1.place(x=0,y=0)

label2 = tk.Label(master=frame1,text='I am at(75,75)',bg='yellow',font='Consolas 20')
label2.place(x=75,y=75)



window.mainloop()