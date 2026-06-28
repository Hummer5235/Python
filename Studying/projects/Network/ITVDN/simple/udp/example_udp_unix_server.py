#
import socket , os

unix_sock_name = 'unix.sock'
sock = socket.socket(socket.AF_UNIX,socket.SOCK_DGRAM )  #AF_UNIX  - , socket.SOCK_DGRAM  - SocketDataGram - UDP

if os.path.exists(unix_sock_name):
    os.remove(unix_sock_name)

sock.bind(unix_sock_name) #Резервируем порт. Привязываем сокет к адресу

while True:
    try:
        result = sock.recv(1024) #получает данные из сокета. Возвращаемое значение - байтовый объект, представляющий полученные данные.
    except KeyboardInterrupt:
        sock.close()
    else:
        print('Message',result.decode('utf-8'))
