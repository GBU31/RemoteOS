from client import Client
from remoteOS import *

ip_and_port = ip_and_port()
c = Client(ip_and_port.get_local_ip(), ip_and_port.get_port())
c.Connect()