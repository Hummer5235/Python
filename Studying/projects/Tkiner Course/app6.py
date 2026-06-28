import tkinter as tk

window = tk.Tk()
window.geometry('600x600')
window.columnconfigure(0,minsize=250)
window.rowconfigure(0,minsize=100)

# frame1 = tk.Frame(master=window,width=500,height=500,bg='black')
# frame1.pack()

lbl1 = tk.Label(text='North')
lbl1.pack(side='top')
# lbl1.grid(row=0,column=0,sticky='ne')

lbl2 = tk.Label(text='South')
lbl2.pack(side='bottom')
# lbl2.grid(row=1,column=0,sticky='sw')

lbl3 = tk.Label(text='West')
lbl3.pack(side='left')
# lbl3.grid(row=2,column=2,sticky='w')


lbl4 = tk.Label(text='East')
lbl4.pack(side='right')
# lbl4.grid(sticky='e')









window.mainloop()