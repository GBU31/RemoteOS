import socket


class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def send(self, data):
        return data.encode()

    def Connect(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))

        while True:
            x = input(f'({self.ip})->')
            s.send(self.send(x))