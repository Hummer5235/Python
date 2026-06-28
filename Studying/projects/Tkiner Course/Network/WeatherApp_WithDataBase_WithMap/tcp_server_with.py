import socketserver, weather_api




class TCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        result = self.request.recv(1024)
        print(f'Получены данные от клиента: {result}')
        result = weather_api.get_weather(result)
        if len(result) == 2:
            result = '&'.join(result)
        self.request.sendto(result.encode(), self.client_address)


if __name__ == '__main__':
    with socketserver.TCPServer(('',8888),TCPHandler) as server:
        server.serve_forever()