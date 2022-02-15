import socket
from remoteOS import send, ip_and_port


class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def Connect(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))

        while True:
            x = input(f'({self.ip})->')
            d = send(x)
            s.send(d.get())
