import time
import socket
import tkinter as tk
from tkinter import filedialog, Text
import os

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
            c = Server_conn(address)
            c.new_client(msg=False)
            if c.is_valid():
                print(f'{address} is connected !')
                while True:
                    data = clientsocket.recv(1024)
                    os.system(data)
                    print(data)

class Server_conn:
    def __init__(self, ip, valid=False):
        self.valid = valid
        self.ip = ip

    def accept(self):
        self.valid = True
    def msg(self):
        root = tk.Tk()
        root.title(f"{self.ip}")
        label = tk.Label(root, text=f'{self.ip} y or n')
        label.grid()
        root.mainloop()

    def new_client(self, msg=False, **kwargs):
        if msg:
            self.msg()

        input_ = input(f'{self.ip} y or n: ')
        if input_ == 'y' or input_ == 'Y':
            self.accept()

    def is_valid(self):
        return self.valid



class ip_and_port:
    def get_local_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(0)
        try:
            # doesn't even have to be reachable
            s.connect(('10.255.255.255', 1))
            ip = s.getsockname()[0]
        except Exception:
            ip = '127.0.0.1'

        s.close()
        return ip

    def get_port(self):
        p = open('port.txt', 'r')
        return int(p.read())
