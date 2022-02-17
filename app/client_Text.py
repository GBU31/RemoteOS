from remoteOS import Client

def Host(host=None):
    if host == None:
        host = '127.0.0.1'
    return host


c = Client(Host(), 8889)
c.Connect()