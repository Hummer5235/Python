import requests, ssl
#
# #Get запросы
#
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.5.704 Yowser/2.5 Safari/537.36",
  }
#
# response = requests.get('https://httpbin.org/get')
# # response = requests.get('https://httpbin.org/headers',headers = headers)
# # response = requests.get('https://127.0.0.1:8888')
#
# print(response.status_code)
# print('--- TEXT ---',response.text,sep='\n')
# print('--- HEADERS ---',response.headers,sep='\n')
# print('--- JSON ---',response.json(),sep='\n')



#Post запросы
data = {
    'custname': 'Hummer5235',
    'custtel': '+79152223535',
    'custemail': 'hummer5235@mail.ru',
    'size' : 'medium',
    'topping': 'bacon',
    'delivery': '19:00',
    'comments': '',
}
# response = requests.post('https://httpbin.org/post',headers = headers,data = data)
# print(response.status_code)
# print('--- TEXT ---',response.text,sep='\n')
# print('--- HEADERS ---',response.headers,sep='\n')
# print('--- JSON ---',response.json(),sep='\n')


data = {
    'login': 'zaharshlykov@mail.ru',
    'auth_token':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzaWQiOiJOMll4T1RJelpHTTFOelZsT0dSaE1qUmpPREJrTkRJNCIsImhhc2giOiI3NzY3ZDUwYWRjYTU4ZTRiIiwiZXhwIjoxNjk1MDI1NTE3fQ.uFoU2yuuRznyLPJiYc18qNTfuFZEVPZU1fCeyGtWR-A'
}


#Для использования сессий
session = requests.Session()

#Необходимо получить токен авторизации
ses = session.post('https://vk.com',data=data)
print(ses.text)
print(ses.status_code)

# print(ses.json())
#Запросы также передаются от текущей сессии
# response = session.post('https://vk.com/feed', data)
# print(response.status_code)
# print('--- TEXT ---',response.text,sep='\n')
# print('--- HEADERS ---',response.headers,sep='\n')
# print('--- JSON ---',response.json(),sep='\n')



