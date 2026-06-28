#Тест сайта httpbin
import webbrowser
import requests
from getpass import getpass
from requests.auth import HTTPBasicAuth

url = 'https://httpbin.org'
# responce = requests.get('https://httpbin.org/get',params={'key':'value'})
# print(responce.text,'get')
# responce = requests.post('https://httpbin.org/post',data={'key':'value'})
# print(responce.text,'post')
# responce = requests.put('https://httpbin.org/put',data={'key':'value'})
# print(responce,'put')
# print(responce.request.body,'put')
# print(responce.headers['content-type'],'put')
# print(responce.request.url,'put')
# responce = requests.delete('https://httpbin.org/delete')
# print(responce,'delete')
# responce = requests.head('https://httpbin.org/get')
# print(responce,'head')
# responce = requests.patch('https://httpbin.org/patch',data={'key':'value'})
# print(responce,'patch')
# responce = requests.options('https://httpbin.org/get')
# print(responce,'options')


response = requests.get('https://api.github.com/Hummer5235',auth=HTTPBasicAuth('Hummer5235',getpass()),timeout=1)
print(response)
print(response.status_code)

# webbrowser.open('https://api.github.com/Hummer5235')

