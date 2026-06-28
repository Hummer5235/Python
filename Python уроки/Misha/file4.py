file = open('new_file.txt','w') # Указываем открытие на запись

# file.write('Hello World!') # Метод для записи в файл

# file.write('Hello\n')

"""При открытии в режимах записи 'w','wt','wb'
Содержимое удаляется и новая инф. записывается поверх"""


file.write('Hello1\n')
file.write('Hello2\n')
file.write('Hello3\n')



'''Для дозаписи инф. в файл используем режим append - 'a' 
Для записи и чтения добавляется знак + '''


file = open('new_file.txt','a+',encoding='utf-8')

file.write('New string\n')
file.write('Новая строка\n')


#После записи возвращаемся в начало, чтобы прочитать

file.seek(0)

print(file.read())

# file.writelines(['Hello4\n','Hello5\n','Hello6\n','Hello7\n'])




file.seek(0)


# for i in file:
# 	print('Задача выполена? ',i,end='')
# 	a = input()
# 	if a.lower() == 'да':
# 		print('Ok')
# 	else:
# 		print('Следующая задача\n')