#Находим номера в тексте
import ph_numbers
import pyperclip


def isPhoneNumber(text):
	if len(text) == 12 and text[:3].isdecimal():
		if text[4:7].isdecimal() and text[3]=='-' and text[7]=='-' and text[8:].isdecimal():
			return True
		else:
			return False
	else:
		return False 

# print(isPhoneNumber('415-555-2127'))
# print(isPhoneNumber('415-555-2t27'))
# print(isPhoneNumber('415-555_2127'))
# print(isPhoneNumber('w15-555-2127'))


message = 'Позвони мне по номеру 415-555-2127. 415-545-9902 Это телефонный номер офиса'

def findPhoneNumber(message):
	for i in range(len(message)):
		chunk = message[i:i+12]
		if isPhoneNumber(chunk):
			print(f'Найденный телефонный номер: {chunk}')
	print('Готово')

# print(findPhoneNumber(message))

text = pyperclip.paste()
print(findPhoneNumber(text))
