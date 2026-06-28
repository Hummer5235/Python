#Чтение и запись в бинарном режиме
import pickle


books = [('1984','Джордж Оруэлл',400),
		 ('Евгений Онегин','А.С.Пушкин',250),
		 ('Мертвые Души','Н.В.Гоголь',190)]

#Бинарный режим записи
file = open('test.bin','wb+')

#Запись и сохранение
pickle.dump(books,file) 


#Бинарный режим чтения
# file = open('test.bin','rb')

#Чтение
# lst = pickle.load(file)


file.seek(0)
lst = pickle.load(file)
print(lst)
