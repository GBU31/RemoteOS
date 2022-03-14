import socket


class Ip_and_Port:
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
        p = open('./core/port.txt', 'r')
        return int(p.read())