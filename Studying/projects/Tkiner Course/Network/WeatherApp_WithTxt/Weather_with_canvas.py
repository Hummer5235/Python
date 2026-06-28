from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import json
import example3_tcp_client

# sys.path.insert(0,'C:/Users/Захар/Desktop/Python/Studying/projects/Network/HubStudio')



window = Tk()
W,H = 500,600
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry(f'{W}x{H}+{width//2-W//2}+{height//2-H//2-50}')
window.resizable(False,False)
window.title('Текущая погода')


color = 'lightblue'
img = Image.open('../../Icons/Village_bg2.jpg')
img = ImageTk.PhotoImage(img)

# bg = Label(image=img)
# bg.place(relx=0.5,rely=0.4,anchor=CENTER)








canv1 = Canvas()
canv1.create_image(-500,-100,image=img,anchor = NW)
canv1.create_text(255,160,text='Погода',font='Consolas 25 bold')
# screen = canv1.create_text(270,330,text='',font='Consolas 15 bold')
screen = Label(canv1,text='',font='Consolas 13 bold',bg=color)

# canv1.place(relx=0.3,rely=0.2)
canv1.pack(fill=BOTH,expand=1)

# lbl = Label(text='Погода',font='Consolas 25 bold',bg=color)
# lbl.place(relx=0.5,rely=0.1,anchor=CENTER)

# ent = Entry(foreground='grey')
# ent.place(relx=0.5,rely=0.35,anchor=CENTER)
# ent.insert(0,'Введите город')





def choose_entry(event):
    ent.delete(0,END)
    ent.config(foreground='black',font='Consolas 13 bold')



def read_history(task_type='read only'):
    global history_list_index
    with open('data.txt', 'r', encoding='utf-8') as file:
        dictionary = json.load(file)
        if task_type == 'read only':
            #Получить список значений городов, начиная с конца. Для combobox - а
            data = [v for v in list(dictionary.values())[::-1]]
            return data
        elif task_type == 'get max index':
            # Получить максимальный индекс городов. Для нумерации (history_list_index) в начале программы
            if len(dictionary) != 0:
                history_list_index = int(max(dictionary))
            else:
                history_list_index = 0
        else:
            # Работа с нумерацией городов
            if len(dictionary)>4:
                del(dictionary['1'])
                k = 1
                new_dict = {}

                for v in dictionary.values():
                    new_dict[k] = v
                    k+=1
                dictionary = new_dict
                print(f'new_dict: {new_dict}, max:{max(new_dict)}')

                number = str(max(dictionary) + 1)
                print('Длина словаря больше 3', dictionary, number)
                return dictionary, number
            else:
                history_list_index += 1
                print('Длина словаря меньше 3', dictionary, history_list_index)
                return dictionary,history_list_index

def write_history(dann):
    history_list, history_list_index = read_history('smt')

    with open('data.txt', 'w', encoding='utf-8') as outfile:
        # print(outfile)
        history_list[history_list_index] = dann
        json.dump(history_list,outfile,ensure_ascii=False)
        print(dann)
    data = read_history()
    ent.config(values=data)




def check_weather(event= None):

    city = ent.get()
    result = example3_tcp_client.send_massage(city)
    if len(result)==2:
        weather, temp = result
        write_history(city)
        # print(weather.py)
        screen.config(text=f'{weather}\n{temp}')
    else:
        answer = ''.join(result)
        screen.config(text=f'{answer}')
    screen.place(relx=0.5, rely=0.5, anchor=CENTER)



history_list_index = 0
read_history('get max index')
data = read_history()

ent = ttk.Combobox(values=data)
ent.insert(0,'Введите город')
ent.place(relx=0.5,rely=0.35,anchor=CENTER)

btn = Button(text='Узнать погоду',font='Consolas 15 bold',bg=color,relief=RAISED,borderwidth=5,
             command=check_weather)
btn.place(relx=0.5,rely=0.7,anchor=CENTER)
ent.bind('<Button-1>',choose_entry)
ent.bind('<Return>',check_weather)

print(read_history())


window.mainloop()