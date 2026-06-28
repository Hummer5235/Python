
import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM )
sock.bind(('127.0.0.1',8888))
sock.listen(5)
sock.setblocking(False) #Неблокирующий режим.
while True:
    try:
        client, addr = sock.accept()
    except socket.error:
        print('Клиент не подключился')
    else:
        # client.setblocking(True)
        result = client.recv(1024)
        print('Message',result.decode('utf-8'))
        client.close()