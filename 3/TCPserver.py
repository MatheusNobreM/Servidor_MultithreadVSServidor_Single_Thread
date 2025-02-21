from socket import *
import threading

class TCPserver:
    def __init__(self, server_port: int):
        self.server_port = server_port
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        self.server_socket.bind(('', self.server_port))
        self.server_socket.listen(5)

    def start(self, handler_function):
        print(f"Servidor escutando na porta {self.server_port}")
        while True:
            connection_socket, addr = self.server_socket.accept()
            print(f"Conexão estabelecida com {addr}")
            threading.Thread(target=self.handle_client, args=(connection_socket, handler_function)).start()

    def handle_client(self, connection_socket, handler_function):
        request = self.getRequest(connection_socket)
        response = handler_function(request)
        self.sendResponse(connection_socket, response)
        connection_socket.close()

    def getRequest(self, connection_socket) -> str:
        return connection_socket.recv(1024).decode('utf-8')

    def sendResponse(self, connection_socket, response: str) -> None:
        connection_socket.send(response.encode('utf-8'))
