#Регулярные выражения 
#Компактное описание тектовых шаблонов
import re , pyperclip , ph_numbers


text = pyperclip.paste()

#Возвращает объект переданного регулярного выражения - Regex
#\d - Цифровойсимвол
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  
# print(phoneNumRegex)

for i in range(len(text)):
	
	#Передача методу search об. Regex строки, в которой выполняется поиск
	mo = phoneNumRegex.search(text)
	#Метод group() - объекта Match, вернет строку, содерж фактически найденный текст
	print(f'Найденный телефонный номер: {mo.group()}')

mo = phoneNumRegex.search('Мой номер: 415-555-4242.')
print(f'Найденный телефонный номер: {mo.group()}')