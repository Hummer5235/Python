#Конвертер температуры
import tkinter as tk

window = tk.Tk()
window.title('Temperature converter')
window.geometry('400x50')

def convert_temperature():
    fahrenheit = ent_temp.get()
    celsius = (5 / 9) * (float(fahrenheit) - 32)
    lbl_temp_c['text'] = str(round(celsius,1))+' C°'


ent_temp = tk.Entry(width=20)
ent_temp.grid(row=0,column=0,padx=10)

lbl_temp_f = tk.Label(text='F°')
lbl_temp_f.grid(row=0,column=1)

btn_temp_convert = tk.Button(text='-->',relief=tk.RAISED,borderwidth=3,command=convert_temperature,width=5)
btn_temp_convert.grid(row=0,column=2)

lbl_temp_c = tk.Label(text=f'{0} C°')
lbl_temp_c.grid(row=0,column=3,padx=10)



window.mainloop()