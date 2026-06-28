# Пользователь вводит имя, фамилию, возраст . Создайте словарь user
firstname = input("Enter your firstname: ")
lastname = input("Enter your lastname: ")
age = input("Enter your age: ")

user = dict(firstname = firstname,lastname=lastname,age=age)
print(user)

for key,value in user.items():
	print(key,value)