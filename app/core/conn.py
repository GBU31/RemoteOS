import tkinter as tk
from tkinter import filedialog, Text

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

    def new_client(self, **kwargs):
        input_ = input(f'{self.ip} y or n: ')
        if input_ == 'y' or input_ == 'Y':
            self.accept()

    def is_valid(self):
        return self.valid