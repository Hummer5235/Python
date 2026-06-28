file = open('file3.txt','a+',encoding='utf-8')

file.write('Hello1')
file.write('Hello2')

file.seek(0)
print(file.read())


file.close()



