import socket


class GraphiteBackend:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def connect(self):
        self.sock = socket.socket()
        self.sock.connect((self.host, self.port))

    def store(self, message):
        self.sock.sendall(message.encode())

