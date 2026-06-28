from urllib import request

response = request.urlopen('http://example.com')

print(response.status)
print(response.getcode())
print(response.msg)
print(response.reason)
# Получение заголовков в виде внутреннего объекта
print('--- Headers ---')
print(response.headers)
# Получение словаря всех заголовков
print(response.getheaders())
#Получение заголовка
print(response.headers.get('Content-Type'))
print(response.getheader('Content-Type'))
