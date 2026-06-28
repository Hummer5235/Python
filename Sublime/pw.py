#! python3
# pw.py - Программа для незащищенного хранения паролей

PASSWORDS = {"email":"zaharshlykov@mail.ru",
			 "blog":"newParol"
}

import sys
if len (sys.argv) <2:
	print("Использование: pw.py [имя учетной записи] - копирование пароля учетной записи")
	sys.exit()
account = sys.argv[1]  # Первый аргумент командной строки это имя учетной записи