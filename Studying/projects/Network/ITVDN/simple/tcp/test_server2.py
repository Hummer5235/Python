
import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # socket.SOCK_STREAM - сокет TCP протокола
sock.bind(('',8888))
sock.listen(5) # Количество прослушиваемых соединений для очереди


message = '''hello world\n
Hello from Hummer5235'''

while True:
    try:
        c , addr = sock.accept() # Ждем и принимаем клиента из очереди. Клиентский сокет и адрес
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        result = c.recv(1024)
        print(result)
        print('Got connection from')
        c.send(('HTTP/1.1 200 OK\n\n'+message).encode())
        c.close()














    # with open('answer2.html','rb') as file:
    #     data = file.read(2048)
    #     while data:
    #         client.send(data)
    #         data = file.read(2048)

    # client.sendto('Клиент, ты был подключен'.encode(),addr)

# print('Message',result.decode('utf-8'))
