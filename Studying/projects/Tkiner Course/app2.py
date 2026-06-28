import tkinter as tk
#relief - Стиль рамки
#borderwidth - ширина ободка

window = tk.Tk() # Создаем окно - экз класса Tkinter
window.iconbitmap('Icons/accessoriestexteditoricon.ico')

frame_a= tk.Frame(relief=tk.GROOVE,borderwidth=5)
label_a = tk.Label(master=frame_a,text='I am in Frame A',width=50)
label_a.pack()

frame_b= tk.Frame(relief=tk.GROOVE,borderwidth=5)
label_b = tk.Label(master=frame_b,text='I am in Frame B',width=50)
label_b.pack()


frame_a.pack()
frame_b.pack()




window.mainloop()

