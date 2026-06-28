import re , os

os.system('CLS')

text = '<font color=#CC0000>'



match = re.findall(r'(\w+)=(#[\da-fA-F]{6}\b)',text)
match2 = re.search(r'(\w+)=(#[\da-fA-F]{6}\b)',text)
match3 = re.search(r'(?P<key>\w+)=(?P<value>#[\da-fA-F]{6}\b)',text)

print(match)
print(match2)

#Метод group объекта match. Получаем конкретную сохраняющую группу
print('Группы по отдельности: ', match2.group(0),match2.group(1), match2.group(2))
print('Все группы: ', match2.groups())
print('Количество групп: ',match2.lastindex)


print('Получить индекс начала вхождения группы и окончания: ', match2.start(1), match2.end(1))
print('Получить индекс начала вхождения группы и окончания: ', match2.span(1))

print('Получить индекс до которого прошла проверка "search" : ', match2.endpos)
print('Получить индекс с которого началась проверка "search" : ', match2.pos)

print('Возвращение скомпилированного шаблона: ', match2.re)
print('Возвращение анализируемой строки: ', match2.string)

#Для использования этого метода нужно использовать именованные группы
print( match3.groupdict())
#Можно формировать строку с использованием сохраненных групп:
print( match3.expand(r'\g<key>:\g<value>'))



#Метод search - используется для поиска первого вхождения
text = '<font color=#CC0000 bg=#ffffff>'
match = re.search(r'(?P<key>\w+)=(?P<value>#[\da-fA-F]{6}\b)',text)
print(match)

#Метод finditer - возвращает итерируемый объект для перебора всех найденных значений
print('\n','Метод finditer: ')
for match in  re.finditer(r'(?P<key>\w+)=(?P<value>#[\da-fA-F]{6}\b)',text):
	print(match)


#Метод findall - возвращает список найденных вхождений, не объект match
print('\n','Метод findall: ')
match = re.findall(r'(?P<key>\w+)=(?P<value>#[\da-fA-F]{6}\b)',text)
print(match)
