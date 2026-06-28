names=["Ivan","Sergey","Fedor","Yaroslav"]

name=input("Введите имя: ")

#Добавление в конец списка метод append()
names.append(name)

removed=names.pop()

print(names)

print(f"removed = {removed}")

names.pop(0)

print(names)