#Продукты гостей
allGuests = {'Alice':{'apples':5,'pizza':3},
			'Bob':{'ham sandwiches':5,'apples':3},
			'Mariya':{'cups':3, 'apple pies': 1},
			'Nikolya':{'pizza':2, 'apple pies': 3},}




# for k,v in allGuests.items():
# 	print(f'Гость: {k}')
# 	for i,p in allGuests[k].items():
# 		print(i,p)
# 	print()


def products(product):
	counter = 0
	for v in allGuests.values():
		counter += v.get(product,0)

	print(f'Количество {product}',counter)

products('apples')
products('pizza')
products('cups')