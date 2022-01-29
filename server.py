import socket
import os
from remoteOS import *

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        
    def start(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.host, self.port))
        s.listen(1)
        print(self.host, self.port)
        
        while True:
            clientsocket, address = s.accept()
            print(f"{address}")
            c = server(address)
            c.new_client(msg=True)
            if c.is_valid():
                print(f'{address} is connected !')
                while True:
                    data = clientsocket.recv(1024)
                    os.system(data)
                    print(data)


class Server_Text:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        
    def start(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.host, self.port))
        s.listen(1)
        print(self.host, self.port)
        
        while True:
            clientsocket, address = s.accept()
            print(f"{address}")
            c = server(address)
            c.new_client(msg=False)
            if c.is_valid():
                print(f'{address} is connected !')
                while True:
                    data = clientsocket.recv(1024)
                    os.system(data)
                    print(data)
        



