#Переводчик
from tkinter import *

import googletrans
from googletrans import Translator, constants

# print(googletrans.LANGUAGES) # Получить словарь с языками

window = Tk()
window.title('Переводчик')
window.geometry('650x700')
window.resizable(False,False)
window.config(bg='black')
window.rowconfigure((0,1,2,3,4),minsize=30)
window.columnconfigure((0,1,2,3,4),minsize=10)


def translate():
    global translator
    text = text_box_input.get('1.0',END)
    text = translator.translate(text)
    text_box_output.delete('1.0',END)
    text_box_output.insert(END,text.text)



translator = Translator()
label = Label(text='Введите текст',fg='white',bg='black',font=('Comic Sans MS',15))
label.grid(row = 0, column=0,sticky=W)

text_box_input = Text(width=40,height=10,font=('Comic Sans MS',15),wrap=WORD)
# text_box_input.insert('1.0','Текст для перевода')
text_box_input.grid(row=1,column=0,sticky=W)

btn = Button(text='Перевести',command=translate,relief=RAISED,borderwidth=5,bg='#abc930',fg='black',font='20',width=10,height=3,activebackground='#eaff00')
btn.grid(row=1,column=1,padx=20)

label2 = Label(text='Перевод',fg='white',bg='black',font=('Comic Sans MS',15))
label2.grid(row = 2,column=0,sticky=W)



text_box_output = Text(width=40,height=10,font=('Comic Sans MS',15),wrap=WORD)
# text_box_output.insert('1.0','Переведенный текст')
text_box_output.grid(row=3,column=0,sticky=W)



# result = translator.translate('Mitä sinä teet')
# print(result)
window.mainloop()