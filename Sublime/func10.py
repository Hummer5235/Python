#Вывод слова лесенкой
def strings(word):
	for i in range(len(word)):
		print((i+1)*word[i])

strings("HelloWorld!")