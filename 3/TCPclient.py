from socket import *

class TCPClient:
    def __init__(self, server_name: str, server_port: int):
        self.server_name = server_name
        self.server_port = server_port
        self.client_socket = None

    def connect(self):
        self.client_socket = socket(AF_INET, SOCK_STREAM)
        self.client_socket.connect((self.server_name, self.server_port))

    def sendRequest(self, request: str) -> None:
        self.client_socket.send(request.encode('utf-8'))

    def getResponse(self) -> str:
        return self.client_socket.recv(1024).decode('utf-8')

    def close(self) -> None:
        self.client_socket.close()
