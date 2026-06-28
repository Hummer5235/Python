#Использование html
from tkinter import *
from tkhtmlview import HTMLLabel
from tkinter import ttk
from PIL import Image,ImageTk


window = Tk()
window.geometry('500x500')
window.title('Использование html')

tabs = ttk.Notebook()

frm1 = Frame()
tabs.add(frm1,text='Заголовки')

frm2 = Frame()
tabs.add(frm2,text='Параграфы')


frm3 = Frame()
tabs.add(frm3,text='Списки')

frm4 = Frame()
tabs.add(frm4,text ='Ссылки')

my_label = HTMLLabel(frm1,html='''
    <h1>Заголовок</h1>
    <h2>Заголовок</h2>
    <h3>Заголовок</h3>
    <h4>Заголовок</h4>
    <h5>Заголовок</h5>
    '''
)
my_label.pack()

my_label2 = HTMLLabel(frm2,html='''
    <mark><i><b><p1>Параграф</p1></b></i></mark>
    
    '''
)
my_label2.pack()

my_label3 = HTMLLabel(frm3,html='''
    <ul>
        <li>Один</li>
        <li>Два</li>
        <li>Три</li>
    </ul>
    
    <ol>
        <li>Один</li>
        <li>Два</li>
        <li>Три</li>
    </ol>
    
    
    '''
)


my_label3.pack()


bg_img = Image.open('../Icons/bg_image.jpg').resize((500,500))
bg_img = ImageTk.PhotoImage(bg_img)

lbl4_bg =Label(frm4,image=bg_img)
lbl4_bg.grid(row=0,column=0)

my_label4 = HTMLLabel(frm4,html='''
    <body>
        <style>
            body {
                background: 
                }
        </style>
    </body>
    
    
    <ol>
        <h4>Колледжи Владимирской области</h4>
        <li><a href = "http://t917315.spo.obrazovanie33.ru/">Киржачский машиностроительный колледж</a></li>
        <li><a href = "http://амк33.рф/">Александровский медицинский колледж</a></li>
        <li><a href = "http://кольчугпк.рф/">Кольчугинский политехнический колледж</a></li>
    </ol>
    <img src = '../Icons/bg_image.jpg' width=500 height = 300>
    ''')
my_label4.place(rely=0,relx=0)


tabs.pack()
window.mainloop()