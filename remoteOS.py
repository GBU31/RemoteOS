import time
import socket


class server:
    def __init__(self, ip, valid=False):
        self.valid = valid
        self.ip = ip

    def accept(self):
        self.valid = True
    def msg(self):
        import tkinter as tk
        from tkinter import filedialog, Text

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




class send:
    def __init__(self, data):
        self.data = data

    def get(self):
        return self.data.encode()

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
