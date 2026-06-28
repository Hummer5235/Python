import requests , socket
import datetime as dt


responce = requests.get('http://127.0.0.1:2000/request')
print(responce.status_code)
print(responce.text)






# responce2 = requests.post('http://127.0.0.1:2000/',data=data)