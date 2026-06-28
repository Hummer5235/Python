#Срезы строк
string = 'Длинношеее животное'
print('1st element is',string[0] )
print(string[0:3])
print(string[3:7])
print(string[11:]) #Не указан конец
print(string[:10]) #Не указано начало
print()

#Отрицательные индексы
print("Отрицательные индексы:")
print(string[-8:])
print(string[:-9])

#Шаг
print(string[:5:1])
print(string[::-1])
