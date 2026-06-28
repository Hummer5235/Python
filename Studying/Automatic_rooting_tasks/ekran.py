spam = 'Say hi to Bob\'s mother'
print(spam)



#Сырая строка

spam = 'Say hi to Bob\'s mother'
print(spam)


#Методы строк 
print('Из букв , не пустая','Hello'.isalpha())
print('Из букв и цифр, не пустая',"Чтозацифры123".isalnum())
print('Из цифр, не пустая',"Чтозацифры123".isdecimal())


str1 = 'Hello for everyone'
print(str1.startswith('Hello')) # Как начинается
print(str1.endswith('one')) # Как оканчивается



#Ряд строк в виде списка объединить в одну строку
print(', '.join(['cats','dogs','animals']))
print(' '.join(['My','name','is','Simon']))

#Строку разбить на отдельные строки в список 
print('My name is Simon'.split())


spam = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled 'Milk Experiment'

Please do not drink it.
Sincerely,
Bob
'''

print(spam.split('\n'))


#Выравнивание влево, вправо
print('Hello'.rjust(10))
print('Hello'.ljust(10))
print('Hello'.center(10))

print('Hello'.rjust(10,'*'))
print('Hello'.ljust(10,'*'))
print('Hello'.center(10,'*'))




#Пример предметы для пикника
#Используя эти методы можно красиво выровнять строки

def printPicnic(itemsDict, leftWidth, rightWidth):
	print()
	print('PICTIC ITEMS'.center(leftWidth+rightWidth,'-'))
	for k,v in itemsDict.items():
		print(f"{k.ljust(leftWidth,'.')} {str(v).rjust(rightWidth)}")


picnicItems = {'sandwiches':4, 'apples':12, 'cups':4, 'cookies':8000}


printPicnic(picnicItems,12,5)
printPicnic(picnicItems,20,6)



#Методы изменения строки (удаления из нее)
spam = ' Hello World '
print(spam.strip())
print(spam.lstrip())
print(spam.rstrip())

spam2 = 'pHellop'
print(spam2.strip('opHe'))


'''Модуль pyperclip позволяет копировать в буфер обмена компьютера и выполнять оттуда вставку 
'''

import pyperclip

# pyperclip.copy("Wth")
print(pyperclip.paste())
