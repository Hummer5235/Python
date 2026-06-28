# st = 'hello world'
st =''.join(['Бабушка','20 Марта','Егор','12 Марта','Папа','11 Апреля'])
file = open('new_file2.txt','w',encoding='utf-8')
binary = ' '.join(format(ord(x), 'b') for x in st)
file.write(binary)
