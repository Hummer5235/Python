#TCP протокол
#Надежный протокол
#Порядок пакетов соблюдается
# Рукопожатие перед установкой соединения
# Обмен данными
import socket
import weather_api

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # socket.SOCK_STREAM - сокет TCP протокола
sock.bind(('127.0.0.1',8888))
# sock.bind(('192.168.31.96',8888))
sock.listen(5) # Количество прослушиваемых соединений для очереди


while True:
    try:
        client , addr = sock.accept() # Ждем и принимаем клиента из очереди. Клиентский сокет и адрес
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        result = client.recv(1024)
        print(f'Получены данные от клиента: {result}')
        result = weather_api.get_weather(result)
        if len(result)== 2:
            result = '&'.join(result)
        client.sendto(result.encode(),addr)
        client.close()
        # print()
        # print(result.decode('utf-8'))
