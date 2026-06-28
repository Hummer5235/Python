# #Функции как объекты
#
#
# num = 17
# numbers = [1,2,3,4,5]
# colors = (1,2,3)
# name = 'Python'
#
# print(type(num))
# print(type(numbers))
# print(type(colors))
# print(type(name))
#
# print(type(print))
# print(type(len))
# print(type(sum))
#
#
# def hello():
#     print('Hello from function!')
#
# func = hello # Присваиваем переменной func ф-ию hello
# func()
#
#
#
# def start():
#     print('start')
#
# def stop():
#     print('stop')
#
# def pause():
#     print('pause')
#
# commands = {'start':start,'stop':stop,'pause':pause}
# command = input()
# commands[command]() # Вызываем нужную ф-ию по ключу
#
# # if command == 'start':
# #     start()
# # elif command == 'stop':
# #     stop()
# # elif command == 'pause':
# #     pause()
#
#
# #-----------------Функции в качестве аргументов других функций-----------------------
# #min()
# #max()
# #sorted()
#
numbers = [10,-15,-5,3,14]
# numbers.sort()
print(sorted(numbers,key=abs))
print(min(numbers,key=abs))
print(max(numbers, key=abs))
print(numbers)

#Компаратор(compare) - функция , определяющая условия сравнения элементов




