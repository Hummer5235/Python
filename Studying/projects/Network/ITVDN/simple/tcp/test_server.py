#TCP протокол
#Надежный протокол
#Порядок пакетов соблюдается
# Рукопожатие перед установкой соединения
# Обмен данными
import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # socket.SOCK_STREAM - сокет TCP протокола
sock.bind(('192.168.31.96',8888))
sock.listen(5) # Количество прослушиваемых соединений для очереди


while True:
    try:
        client , addr = sock.accept() # Ждем и принимаем клиента из очереди. Клиентский сокет и адрес
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        result = client.recv(1024) #Получение данных от клиента
        client.sendto('Клиент, ты был подключен'.encode(),addr)
        client.close()
        print('Message',result.decode('utf-8'))
