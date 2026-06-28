from tkinter import *


window = Tk()
window.title('Работа с Canvas')
window.geometry('300x200')

c = Canvas(width=200,height=200,bg='white')
c.pack()

triangle = c.create_polygon(10,50,80,50,45,10)

rectangle = c.create_rectangle(10,10,190,60,
                               fill='orange',
                               outline='green',
                               width=5)

line = c.create_line(10,10,190,190,
                     fill = 'green',
                     width=5,
                     arrow=LAST,
                     activefill='lightgreen')





window.mainloop()