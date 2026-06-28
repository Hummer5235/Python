friends = {'Max':10,'Misha':13,'Alex':15,'Anna':8}


#get - получить значение из словаря или вернуть фразу
print(friends.get('Kolya','Возраста нет'))
print(friends.get('Alex','Возраста нет'))


#setdefault - получить значение из словаря или сохранить с новым значением
print(friends.setdefault('Kolya',3))
print(friends.setdefault('Alex',5))

print(friends)