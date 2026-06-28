import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM )  #AF_INET  - IP V4 , socket.SOCK_DGRAM  - SocketDataGram - UDP
sock.bind(('127.0.0.1',8888)) #Резервируем порт. Привязываем сокет к адресу
result = sock.recv(1024) #получает данные из сокета. Возвращаемое значение - байтовый объект, представляющий полученные данные.
print('Message',result.decode('utf-8'))
sock.close()