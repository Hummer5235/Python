#mcb.pyw - Сохраняет и загружает фрагменты текста в буфер обмена.
#Использование:	 py.exe mcb.pyw save <ключевое слово> - Сохраняет буфер обмена в ключевое слово.
#				 py.exe mcb.pyw <ключевое слово> - Загружает ключевое слово в буфер обмена.
#				 py.exe mcb.pyw list - Загружает все ключевые слова в буфер обмена.

import shelve, pyperclip, sys
mcbShelf = shelve.open('mcb') 




print(len(sys.argv))
#Сохранение содержимого в буфер обмена
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
	mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
	if sys.argv[1].lower() == 'list':
		pyperclip.copy(str(list(mcbShelf.keys())))
	elif sys.argv in mcbShelf:
		pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()