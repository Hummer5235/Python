import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('192.168.31.96',25565))
server.listen(5)
# number = 0|



while True:
    try:
        client_socket, client_address = server.accept()
    except ValueError:
        pass
    else:
        print(client_address)
        data = client_socket.recv(2048)
        # number += 1
        with open('server_image.jpg', mode='wb') as file:
            while data:
                file.write(data)
                data = client_socket.recv(2048)


