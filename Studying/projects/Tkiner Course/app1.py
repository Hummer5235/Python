import tkinter as tk
#Окно -  контейнер, в которых находятся все GUI элементы.
#Виджеты - текстовые боксы, ярлыки и кнопки. Помещаются внутрь окон

window = tk.Tk() # Создаем окно - экз класса Tkinter

#Добавляем виджеты
label = tk.Label(text='Привет, Tkinter!',fg='deep sky blue',bg='black',width=20,height=10,font='Arial 25')
button = tk.Button(text='Жмякни сюда',fg='deep sky blue',bg='black',width=20,font='Arial 25')
label_name = tk.Label(text='Имя')
entry = tk.Entry() #Виджет entry для ввода текста
text_box = tk.Text()
frame = tk.Frame() # Виджет рамки



label.pack()
button.pack()
label_name.pack()
entry.pack()
# text_box.pack()
frame.pack()

entry.insert(0,'!Shlykov') #Вставляет текст на указанную позицию
entry.delete(0) #Удаляет элементы по номеру. Также можно сделать срез
name = entry.get() #Получить значение из однострочного виджета
text_box.insert(0.0,'Text')
text_box.insert(tk.END,'\nNew')
text = text_box.get(1.0,1.5) # Получить текст из text_box
all_text = text_box.get(1.0,tk.END)

print(name)


window.mainloop()

