# Широковещательное сообщение всем
import socket

sock =socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#255.255.255
sock.bind(('',8888))
# sock.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1) # Широковещательное сообщение
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

while True:
    result = sock.recv(1024)
    print('Message:',result.decode('utf-8'))