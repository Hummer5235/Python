print('Мне нужно купить продукты в магазине')
print('Я решил составить список:')

products = []
print(f'Сейчас в списке {len(products)} продукт(-ов)')

'''
Спросить сколько продуктов хотим записать
Сохранить нужное кол-во продуктов в список
'''

kolichestvo = int(input('Введите кол-во продуктов: '))
for i in range(kolichestvo):
	product = input('Введите продукт: ')
	products.append(product)

print(products)
print(f'Сейчас в списке {len(products)} продукт(-ов)')


print()
answer = input("Хотите добавить в список что нибудь еще?")
if answer.lower() == 'да':
	products.append(input('Введите продукт: '))

print('Список продуктов готов:',products)

print()
print('Мы пришли в магазин')

while input('Ты купил что нибудь?').lower() == 'да': 
	print()
	answer2 = input("Что ты купил?")
	if answer2 in products:
		products.remove(answer2)
	print(products)
	print()

if len(products)>0:
	print(f'Осталось еще купить {products}')
else:
	print('Молодец, пошли домой')




				