import socket



client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',8888))



with open('img.jpg', 'rb') as file:
    data = file.read(2048)
    while data:
        client.send(data)
        data = file.read(2048)


