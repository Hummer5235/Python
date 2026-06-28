names = {'Alex':15, 'Tim':13, 'Anna':22}

for i in names:
	print(i)
print()

print('Ключи: ')
#keys() - получение ключей
for i in names.keys():
	print(i)
print()

print('Значения: ')
#values() - получение ключей
for i in names.values():
	print(i)
print()

print('Пары ключ - значение: ')
#items() - получение ключей
for k,v in names.items():
	print(k,v)