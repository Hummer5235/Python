
import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM )  #AF_INET  - IP V4 , socket.SOCK_DGRAM  - SocketDataGram - UDP
sock.bind(('127.0.0.1',8888)) #Резервируем порт. Привязываем сокет к адресу

while True:
    try:
        result = sock.recv(1024) #получает данные из сокета. Возвращаемое значение - байтовый объект, представляющий полученные данные.
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        print('Message',result.decode('utf-8'))
