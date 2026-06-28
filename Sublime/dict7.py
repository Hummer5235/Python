# Когда полезно использовать словарь
# 1. Подсчет кол-ва повторяющихся элементов (объектов)

# d ={}

# str ="aasa"

# for l in str:
# 	d[l]=d.setdefault(l,0)+1
	
# print(d)

# 2. Замена разряженного списка 

# 3. Установить соответствие между объектами

# words = {}
# while True:
# 	s =input()
# 	if s in words:
# 		print(f"Слово {s} переводится как {words[s]}")
# 	else:
# 		words[s] = input("Введите перевод слова ")

# 4. Хранение данных об объекте

contacts = {"Alex":{"birthday": "21 may 1988","city":"Kirov"},
			"Stepan":{"birthday": "12 july 1970","city":"Vladimir"},
			"Nikolya":{"birthday": "5 oct 2000","city":"Kostroma"}
}

# Вариант 1
for person in contacts:
	birthday = contacts[person]["birthday"]
	city = contacts[person]["city"]
	print(person,birthday,city,sep="\n",end="\n\n")

# Вариант 2
for person in contacts:
	print(person)
	for data in contacts[person]:
		print(data,contacts[person][data])
	print()