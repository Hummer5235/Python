#Генератор безопасных паролей
from random import *

digits= '0123456789'
lowercase_letters= 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation= '!#$%&*+-=?@^_'


chars = ''

amount = int(input('Введите кол-во паролей для генерации: '))
length = int(input('Введите желаемую длину пароля: '))
d = input('Включать ли цифры 0123456789?: ')
ul = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?: ')
ll = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?: ')
p = input('Включать ли символы !#$%&*+-=?@^_?: ')
similar_chars = input('Исключать ли неоднозначные символы il1Lo0O?')

lst_answers = [d,ul,ll,p]
lst_simbols = [digits,uppercase_letters,lowercase_letters,punctuation]
for i in range(len(lst_answers)):
	if lst_answers[i].lower() =='да':
		chars += lst_simbols[i]
	if similar_chars.lower() == 'да':
		for c in 'il1Lo0O':
			chars = chars.replace(c,'')

def generate_password(length,chars):
	password = ''
	for i in range(amount):
		for j in range(length):
			password += choice(chars)
		return password

for _ in range(amount):
	print(generate_password(length,chars))








	
