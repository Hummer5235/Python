#TCP протокол
#Надежный протокол
#Порядок пакетов соблюдается
# Рукопожатие перед установкой соединения
# Обмен данными
import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # socket.SOCK_STREAM - сокет TCP протокола
sock.connect(('192.168.31.96',8888))
sock.send(b'New message')
msg = sock.recv(1024)
print(msg.decode())
sock.close()



