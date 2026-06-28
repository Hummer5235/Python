import socket
import datetime as dt
import sys
sys.path.insert(0, '/Studying/projects/Network/HubStudio')
from file2 import get_weather


weather, temp = get_weather('Кострома')
print(weather,temp)


def start_my_server():
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #Чтобы сокет был серверным, ему нужно назначить ip
    server.bind(('127.0.0.1',2000))
    server.listen(50)
    while True:
        print('Working...')
        #Принимаем отправленные запросы и разделяем их на клиента и адрес
        client_socket, address = server.accept()
        data = client_socket.recv(1024).decode('utf-8')
        print(data)
        time = str(dt.datetime.now())
        print(type(str(time)))


        HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
        content ='\nГород Кострома\n'.encode('utf-8')
        client_socket.send(HDRS.encode('utf-8')+content)
        # content ='Город Кострома'.encode('utf-8')
        client_socket.send(content)
        # content ='Город Кострома'.encode('utf-8')
        client_socket.send(content)
        client_socket.shutdown(socket.SHUT_WR)


if __name__ == '__main__':
    start_my_server()

