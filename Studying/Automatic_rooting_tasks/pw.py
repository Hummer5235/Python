
#pw.py - Программа незащищенного хранения паролей

import sys, pyperclip
import os

PASSWORDS = {'email':'F7hgv037!.34',
			  'blog':'1389Forgotgot',
			  'luggage':'12345',
			  'vk':'aG.89LkdERF77.'}

#print(__file__)
#print(os.path.basename(__file__))

print(sys.argv)

if len(sys.argv) < 2 :
	print('Использование: python pw.py [имя учетной записи] \
- копирование пароля учетной записи')
	sys.exit()



account = sys.argv[1].lower() # Первый аргумент командной строки - это
					  #Имя учетной записи

if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account])
	print(f'Пароль для {account} скопирован в буфер')
else:
	print(f'Учетная запись {account} отсутствует в списке')