#Простой текстовый редактор
import tkinter as tk
from tkinter.filedialog import askopenfilename,asksaveasfilename

def open_file():
    #Открывает файл для редактирования
    filepath = askopenfilename(filetypes=[('Text Files','*.txt'),('All Files','*.*')])
    if not filepath:
        return None
    txt_edit.delete('1.0',tk.END)
    with open(filepath,'r',encoding='utf-8') as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END,text)
    window.title(f'Простой текстовый редактор {filepath}')
#
def save_file():
    filepath = asksaveasfilename(
        defaultextension='txt',
        filetypes=[('Текстовые файлы','*.txt'),('Все файлы','*.*')])
    if not filepath:
        return None
    with open(filepath,'w',encoding='utf-8') as output_file:
        text = txt_edit.get('1.0',tk.END)
        output_file.write(text)
    window.title(f'Простой текстовый редактор {filepath}')

window = tk.Tk()
window.title('Текстовый редактор')
window.rowconfigure(0, minsize=800)
window.columnconfigure(1, minsize=800,weight=1)




txt_edit = tk.Text(window)
frm_buttons = tk.Frame(window)
btn_open = tk.Button(frm_buttons,text='Открыть',relief=tk.RAISED,borderwidth=3, command=open_file)
btn_save = tk.Button(frm_buttons,text='Сохранить как...',relief=tk.RAISED,borderwidth=3, command=save_file)

btn_open.grid(row=0,column=0,sticky='ew',padx=5,pady=5)
btn_save.grid(row=1,column=0,sticky='ew',padx=5)
frm_buttons.grid(row=0,column=0,sticky='ns')
txt_edit.grid(row=0,column=1,sticky='nswe')






window.mainloop()
