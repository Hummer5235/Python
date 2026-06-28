
#Шифр Цезаря
eng_language = 'abcdefghijklmnopqrstuvwxyz'
rus_language = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

languages = [eng_language,rus_language]

a1 = input('Что будем делать? (шифровать/дешифровать): ')
a2 = input('Какой язык мы используем? (русский/английский): ')
a3 = int(input('Введите шаг сдвига: '))
st = input('Введите слово: ')

st_res = ''


if a2 == 'английский':
	language = languages[0]
	step = 26
elif a2 == 'русский':
	language = languages[1]
	step = 32
if a1 == 'шифровать':
	for i in st :
		if i.isalpha():
			if language.index(i.lower()) + a3 > len(language)-1:
				if i.isupper():
					st_res += language[language.index(i.lower())-step+a3].upper()
				else:
					st_res += language[language.index(i)-step+a3]
			else:
				if i.isupper():
					st_res += language[language.index(i.lower())+a3].upper()
				else:
					st_res += language[language.index(i)+a3]
		else:
			st_res += i

elif a1 == 'дешифровать':
	for i in st :
		if i.isalpha():
			if language.index(i.lower()) - a3 < 0:
				if i.isupper():
					st_res += language[language.index(i.lower())+step-a3].upper()
				else:
					st_res += language[language.index(i)+step-a3]
			else:
				if i.isupper():
					st_res += language[language.index(i.lower())-a3].upper()
				else:
					st_res += language[language.index(i)-a3]
		else:
			st_res += i

print(st_res)

