import tkinter as tk
import random
#Камень ножницы бумага

window = tk.Tk()
window.title('Камень ножницы бумага')
window.geometry('600x400')
window.resizable(width=False,height=False)
window.config(bg='black')

def choose_answer():
    lst = ['Камень','Ножницы','Бумага']
    value = random.choice(lst)
    label['text'] = value



label = tk.Label(window,text='Ответ',foreground='white', font=('Comic Sans',20),bg='black')
label.place(x=200,y=200)

stone = tk.Button(window,
                  text='Камень',
                  font=('Comic Sans',20),
                  command=choose_answer
                  )
stone.place(x=50,y=300)

scissors = tk.Button(window,
                  text='Ножницы',
                  font=('Comic Sans',20),
                  command=choose_answer
                  )
scissors.place(x=225,y=300)

paper = tk.Button(window,
                  text='Бумага',
                  font=('Comic Sans',20),
                  command=choose_answer
                  )
paper.place(x=430,y=300)


window.mainloop()