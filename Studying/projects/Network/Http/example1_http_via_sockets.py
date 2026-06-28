
import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(('example.com',80))
content_items = [
    'GET / HTTP/1.1',
    'Host: example.com',
    'Connection: keep-alive',
    'Accept: text/html',
    '\n'
]

def parse_http_response(text_response):
    lines = text_response.split('\n')
    status_row, lines = lines[0], lines[1:]
    protocol, status_code, message = status_row.split(' ')
    print('Protocol:',protocol)
    print('Status Code:',status_code)
    print('Message:',message)


content = '\n'.join(content_items)
print('--- HTTP MESSAGE ---')
print(content)
print('--- HTTP MESSAGE END ---','\n')
sock.send(content.encode())
result = sock.recv(10024)
print('--- RESULT MESSAGE ---')
print(result.decode())
parse_http_response(result.decode())