import tkinter as tk
import datetime

window = tk.Tk()
window.title('Данные пользователя')
window.geometry('670x350')
window.columnconfigure([0,1,2,3,4,5],minsize=50)

persons = {}
count = 0

def check_line():
    flag = True
    for line in list_of_ent:
        #Если поле пустое - заполняем
        if len(line.get())==0 :
            line.insert(0,'Необходимо заполнить поле')
            flag = False
        #Если поле заполнено - ничего не делаем
        elif line.get()=='Необходимо заполнить поле':
            flag = False
            break

    # start = datetime.datetime.timestamp(datetime.datetime.now())
    # end = datetime.datetime.timestamp(datetime.datetime.now())
    # while True:
    #     end = datetime.datetime.timestamp(datetime.datetime.now())
    #     if end - start > 0.1:
    #         break
    return flag


def send():
    global count
    if check_line():
        for number in range(len(lst)):
            persons[count][lst[number]] = list_of_ent[number].get()
        count += 1
        print('Отправлено')
        clear()
        print(persons)
    # #Очистить таблицу после отправки данных
    # for ent in list_of_ent:
    #     ent.delete(0,tk.END)


def clear(condition = 1):
    if condition == 1:
        for ent in list_of_ent:
            ent.delete(0,tk.END)
    # else:
    #     for ent in list_of_ent:
    #         if len(ent.get())==0:
    #             ent.delete(0,tk.END)
    print('Очищено')


def generate_dict():
    for i in range(10):
        persons[i] = {}
    for j in range(len(persons)):
        for i in lst:
            persons[j][i] = ''

frm_text = tk.Frame()
frm_text.pack()

frame_buttons = tk.Frame(padx=10,pady=10)
frame_buttons.pack(fill=tk.X)

lst = ['Имя','Фамилия','Пол','Адрес1','Адрес2','Город','Регион','Почтовый индекс','Страна']
list_of_ent = []

for i in enumerate(lst):
    lbl = tk.Label(master=frm_text,text=i[1]+':')
    lbl.grid(row=i[0],sticky='w')
    ent = tk.Entry(master=frm_text,width=50)
    list_of_ent.append(ent)
    ent.grid(row=i[0],column=1)

print(list_of_ent)

btn1 =tk.Button(master=frame_buttons,text='Отправить',command=send)
btn1.pack(side= tk.RIGHT,padx=10,pady=10)

btn2 = tk.Button(master=frame_buttons,text='Очистить',command=clear)
btn2.pack(side=tk.RIGHT,padx=10,pady=10)



generate_dict()


print(persons)
window.mainloop()