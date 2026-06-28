import pickle # Модуль для работы с бинарными данными


books = ['Муму','Отцы и дети','Маленький принц',
'Евгений Онегин']

file = open('file4.bin','wb')

pickle.dump(books,file) # Записать в файл в бин виде


file = open('file4.bin','rb')
out = pickle.load(file)  # Прочитать файл в бин виде
print(out)