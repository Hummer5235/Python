a = {'Max':15, 'Alex':14,'Vanya':10}

#get 
print(a.get('Anya','Имени нет в словаре'))
print(a)

#setdefault - проверяет по ключу, если нет - то добавляет в словарь

print(a.setdefault('Timur', 20))
print(a)

print(a.setdefault('Max', 100))
print(a)



