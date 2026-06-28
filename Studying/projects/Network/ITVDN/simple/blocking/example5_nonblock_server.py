#Использование settimeout для указания время ожидания
import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM )
sock.bind(('127.0.0.1',8888))
sock.listen(5)
sock.settimeout(5) # Переходим в блокирующий режим на 5 сек. В случае отсутствия клиентов переходим в неблокирующий
# sock.settimeout(0) -> sock.setblocking(False)
# sock.settimeout(None) -> sock.setblocking(True)


# sock.setblocking(False) #Неблокирующий режим.
t = 0
while True:
    t += 5
    try:
        client, addr = sock.accept()
    except socket.error:
        print(f'Клиент не подключился {t}')
    else:
        # client.setblocking(True)
        result = client.recv(1024)
        print('Message',result.decode('utf-8'))
        client.close()