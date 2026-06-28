import json

#Чтение

str_json =  '{"Бабушка":"20 Марта","Егор":"12 Марта","Папа":"11 Апреля"}'
# print(type(str_json))
data = json.loads(str_json) # Метод считывает строку в формате JSON и возвращает объекты Python
print(type(data),data)


f = open('templates.json',encoding='utf-8')
file_content = json.load(f) # Метод считывает файл в формате JSON и возвращает объекты Python
print(type(file_content),file_content)



f = open('templates.json',encoding='utf-8')
file_content = f.read() # Прочитали файл
templates = json.loads(file_content) # Строку в формате json превратили в объект Python
print(type(templates),templates)


#Запись
cars = ['Mercedes','BMW','Audi','Запорожец','Lada','Mazda']

json_str = json.dumps(cars,ensure_ascii=False)
print(type(json_str),json_str) #метод возвращает строку в формате JSON

f = open('templates.json','w',encoding='utf-8')
f.write(json_str)

