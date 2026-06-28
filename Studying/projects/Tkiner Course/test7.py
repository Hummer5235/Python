from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image

window = Tk()
window.geometry('500x350')
window.resizable(0,0)


tabs = ttk.Notebook()

fr1 = ttk.Frame(tabs)
fr2 = ttk.Frame(tabs)



lbl1 = Label(fr1)
lbl1.pack()


st_pyt = 'Высокоуровневый язык программирования общего назначения с динамической строгой типизацией и автоматическим управлением памятью, ориентированный на повышение производительности разработчика, читаемости кода и его качества, а также на обеспечение переносимости написанных на нём программ. Язык является полностью объектно-ориентированным в том плане, что всё является объектами.'
st_jv = 'Строго типизированный объектно-ориентированный язык программирования общего назначения, разработанный компанией Sun Microsystems. Разработка ведётся сообществом, организованным через Java Community Process; язык и основные реализующие его технологии распространяются по лицензии GPL'

txt1 = Text(lbl1,wrap=WORD,font='Consolas 16')
txt1.insert('1.0',st_pyt)
txt1.pack()

lbl2 = Label(fr2,text='Вкладка 2')
lbl2.pack()

txt2 = Text(lbl2,wrap=WORD,font='Consolas 16')
txt2.insert('1.0',st_jv)
txt2.pack()

pyt_image = Image.open('Icons/python_18894.png').resize((28,28))
pyt_image = ImageTk.PhotoImage(pyt_image)

jv_image = Image.open('Icons/java_icon.png').resize((28,28))
jv_image = ImageTk.PhotoImage(jv_image)


tabs.add(fr1,text='Python',image=pyt_image,compound=LEFT)
tabs.add(fr2,text='Java',image=jv_image,compound=LEFT)


tabs.pack(expand=1,fill=BOTH)



window.mainloop()