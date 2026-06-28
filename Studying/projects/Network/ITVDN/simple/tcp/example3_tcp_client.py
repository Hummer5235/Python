#TCP протокол , Transmission Control Protocol (протокол управления передачей).
# Составляющие:
# Надежный протокол
# Порядок пакетов соблюдается
# Рукопожатие перед установкой соединения
# Обмен данными



import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # socket.SOCK_STREAM - сокет TCP протокола
sock.connect(('127.0.0.1',8888))
sock.send(b'New message')
sock.close()



