from server import Server, Server_Text
from remoteOS import ip_and_port

ip_and_port = ip_and_port()
s = Server_Text(ip_and_port.get_local_ip(), ip_and_port.get_port())
s.start()
