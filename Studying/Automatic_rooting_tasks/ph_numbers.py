#Генерируем файл с номерами и текстом
import random, pyperclip


alphabet = 'abcdefghijklmnopqrstuvwxyz'


def random_word():
	word = ''
	for i in range(10):
		word += alphabet[random.randrange(len(alphabet))]
	return word




def random_number():
	ph_number = ''
	for i in range(3):
		ph_number += str(random.randrange(0,10))
	ph_number+='-'
	for i in range(3):
		ph_number += str(random.randrange(0,10))
	ph_number+='-'
	for i in range(4):
		ph_number += str(random.randrange(0,10)	)
	return ph_number

text = ''

for i in range(100):
	for i in range(10):
		word = random_word()
		text+= word+ " "
	number = random_number()
	text+= number + ' '

pyperclip.copy(text)
# print(text)
