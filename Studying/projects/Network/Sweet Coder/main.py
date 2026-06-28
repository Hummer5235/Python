import socket
import datetime as dt


server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Чтобы сокет был серверным, ему нужно назначить ip
server.bind(('127.0.0.1',2000))
server.listen(4)
print('Working...')




#Принимаем отправленные запросы и разделяем их на клиента и адрес
client_socket, address = server.accept()
data = client_socket.recv(1024).decode('utf-8')
print(data)

time = str(dt.datetime.now())
print(type(str(time)))
data = {'text':'Информация','time':time}


HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
content = (data['text']+' '+data['time']).encode('utf-8')
client_socket.send(HDRS.encode('utf-8')+content)


