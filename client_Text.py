from client import Client

def Host():
    host = input('Host:')
    if host == '':
        host = '127.0.0.1'
    return host


c = Client(Host(), 8889)
c.Connect()