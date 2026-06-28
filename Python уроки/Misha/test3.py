#json - Java Script Object Notation

import json

# names = {'Max':13,'Andrew':10,'Anna':18}
# f = open('test3.json','w')
# json.dump(names,f)

f = open('test3.json','r+')
file_content = json.load(f) #Cчитывает файл в формате JSON и возвращает объект Python
print(type(file_content),file_content)

