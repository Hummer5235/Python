#TCP протокол
#Надежный протокол
#Порядок пакетов соблюдается
# Рукопожатие перед установкой соединения
# Обмен данными
import socket



def send_massage(data):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # socket.SOCK_STREAM - сокет TCP протокола
    sock.connect(('127.0.0.1', 8888))
    if len(data) != 0:
        data = data.encode()
    else:
        data = '0'.encode()
    sock.send(data)
    result = sock.recv(1024).decode('utf-8').split('&')
    print(f'Получены данные от сервера: {result}')
    return result
