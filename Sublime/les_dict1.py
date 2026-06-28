# # Словарь - неупорядоченная коллекция с доступом по ключу
# d = {}  # Пустой словарь
# print (d)

# #Элементы словаря : Ключ и значение
# # Ключ - уникален, значение может повторяться

# d ={1:"apple",2:"mango"}
# print(d)

# # Ключи могут быть разными
# d = {"fruit":"mango",1:[3,5,7]}
# print(d)

# d = {1:{"student1":"Nikolya","student2":"John"},
# 	 2:{"course1":"Computer Science","course2":"Mathematics"}}

# print(d)


car = {"Company":"Toyota",
	   "Model":"Camri",
	   "year":2021
	   }

# Получить значение по ключу
x = car["Model"]
print(x)

#Добавить элемент
car["Owner"] = "Seva"
print(car)