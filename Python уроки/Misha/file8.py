import json
birthdays = {'Бабушка':'20 Марта','Егор':'12 Марта','Папа':'11 Апреля'}

# f = open('birthdays.json','w+')
# json.dump(birthdays,f,ensure_ascii=False)

f = open('birthdays.json','r+',encoding='utf-8')

birthdays = json.load(f)
for n,d in birthdays.items():
	print(n,d)


name = input('Введите имя: ')

if name in birthdays:
	print(f'День рождения у {name} ',birthdays[name])
else:
	print('Такого имени нет')
	date = input('Введите дату рождения: ')
	birthdays[name] = date

# f = open('birthdays.json','w')
f.seek(0)
json.dump(birthdays,f,ensure_ascii=False)
