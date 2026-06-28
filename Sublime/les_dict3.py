# # Фрукты

# K = int(input("Введите количество фруктов: "))
# fruits={}

# for i in range(K):
# 	fruit = input("Название фрукта: ")
# 	count = int(input("Количество: "))
# 	fruits[fruit] = count
# print(fruits)

#
N = int(input("Введите количество друзей: "))
friends = []

for i in range(N):
	name = input("Имя: ")
	age = int(input("Возраст: "))

	friends.append(dict(name = name, age = age))

print(friends)

a = 0
for i in friends:
	print(i["age"])
	if a < i["age"]:
		a = i["age"]

print()