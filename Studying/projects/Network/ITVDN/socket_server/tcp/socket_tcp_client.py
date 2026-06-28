
import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # socket.SOCK_STREAM - сокет TCP протокола
sock.connect(('127.0.0.1',8888))
sock.send(b'New message')
result = sock.recv(64)
print(f'Result:{result.decode()}')
sock.close()




