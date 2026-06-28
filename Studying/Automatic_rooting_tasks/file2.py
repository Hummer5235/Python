#Сохранение переменных с помощью pprint.pformat()
import pprint

cats = [{'name':'Zophie','desc':'chubby'},{'name':'Pooka','desk':'fluffy'}]

s = pprint.pformat(cats) # Получаем строку которую можно записать в файл при помощи обычного метода write

#Файлы можно записывать в python файлы
print(type(s),s)
f = open('myCats.txt','w')
f.write(s)
f.close()
# f.write(cats)

#Также можно использовать функцию print() для записи в файл
# print(s,file = f)

f = open('myCats.txt')
string = f.read()
print(type(string),string)


# myCat = {'name':'Zophie','desc':'chubby'}
# f = open('myCats.py','w')
# print(myCat,file = f)
# f.close()



# import ast

# f = open('myCats.py')
# string = f.read()
# dictionary = ast.literal_eval(string)
# print(type(dictionary),dictionary)

