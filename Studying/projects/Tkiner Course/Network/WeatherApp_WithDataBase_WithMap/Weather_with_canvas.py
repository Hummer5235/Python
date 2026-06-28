from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import sqlite3 as sq
import Yandex, Location
# sys.path.append(r'C:\Users\Захар\Desktop\Python\Studying\projects\Tkiner Course\Network\WeatherApp_WithDataBase')
import example3_tcp_client
# sys.path.insert(0,'C:/Users/Захар/Desktop/Python/Studying/projects/Network/HubStudio')
from Location import get_location
from Yandex import get_picture

window = Tk()
W,H = 500,600
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry(f'{W}x{H}+{width//2-W//2}+{height//2-H//2-50}')
window.resizable(False,False)
window.title('Текущая погода')
color = 'lightblue'
sub_windows = []
lbl = 0

def load_image(src,size=None):
    if size:
        img = Image.open(src).resize(size)
    else:
        img = Image.open(src)
    img = ImageTk.PhotoImage(img)
    return img

img= load_image('Village_bg2.jpg')

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

    with sq.connect('weather.db') as con:
        cur = con.cursor()
        cur.execute('''CREATE table IF NOT EXISTS cities(
        title TEXT
        )''')
        lst = list(map(lambda x: x[0],cur.execute('''SELECT * FROM cities''')))
        dictionary = dict(zip(map(str,range(1,len(lst)+1)),lst))
        # print(dictionary)
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
            if len(dictionary)>=7:
                del(dictionary['1'])
                k = 1
                new_dict = {}

                for v in dictionary.values():
                    new_dict[k] = v
                    k+=1
                dictionary = new_dict
                # print(f'new_dict: {new_dict}, max:{max(new_dict)}')

                number = str(max(dictionary) + 1)
                # print('Длина словаря больше 3', dictionary, number)
                return dictionary, number
            else:
                history_list_index += 1
                # print('Длина словаря меньше 3', dictionary, history_list_index)
                return dictionary,history_list_index

def write_history(dann):
    history_list, history_list_index = read_history('smt')
    with sq.connect('weather.db') as con:
        history_list[history_list_index] = dann
        cur = con.cursor()
        cur.execute('''DROP table IF EXISTS cities''')
        cur.execute('''CREATE table IF NOT EXISTS cities(
        title TEXT
        )''')
        # cur.execute('''CREATE TABLE IF NOT EXISTS cities''')
        for i in history_list.values():
            cur.execute(f'''INSERT INTO cities VALUES('{i}')''')
        # json.dump(history_list,outfile,ensure_ascii=False)
        # print(dann)
    data = read_history()
    ent.config(values=data)

def new_window():
    global sub_windows
    img = load_image('map.png')
    if len(sub_windows) == 0:
        w = Toplevel()
        w.overrideredirect(True)
        w.geometry(f'{500}x{400}+{width//2+280}+{height//2-H//2}')
        w.title("Карта местности")
        sub_windows.append(w)
        lbl = Label(w, image=img)
        lbl.pack(fill=BOTH, expand=True)
    else:
        lbl = sub_windows[0].children['!label']
        print(lbl)
        lbl.config(image=img)
    lbl.image = img






def check_weather(event= None):

    city = ent.get()
    result = example3_tcp_client.send_massage(city)
    if len(result)==2:
        weather, temp = result
        write_history(city)
        # print(weather.py)
        location = get_location(city)
        print(location)
        get_picture(location)
        screen.config(text=f'{weather}\n{temp}')
        new_window()
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

# print(read_history())


window.mainloop()