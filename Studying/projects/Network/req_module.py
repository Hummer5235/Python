import requests

# url = 'https://google.com'
# url = 'https://httpbin.org/get'
url = 'https://youtube.com/results'
query = {'search_query':'audi'}


#Запрос на получение данных
response = requests.get(url,params=query)

print(response.status_code)
print(response.text,'text')
print(response.url,'url')


#Другие запросы

url = 'https://youtube.com/results'
query = {'search_query':'audi'}

response = requests.post(url,data=query) # Запрос на передачу данных
response = requests.put(url,data=query) # Добавление или изменение данных
response = requests.delete(url,data=query) # Удаление данных
response = requests.patch(url,data=query)
response = requests.options(url,data=query)

print(response.status_code)
print(response.text,'text')
print(response.url,'url')
print(response.headers,'headers')
print(response.headers['Content-Type'])



response = requests.get('https://api.github.com/user')
# print(response.status_code)
# # print(response.text,'text')
# # print(response.url,'url')
# print(response.json(),'json')
print(response.headers)

print(response.headers['Content-Type'])




