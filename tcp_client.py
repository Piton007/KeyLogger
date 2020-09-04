import socket
import sys


class Socket():
    def __init__(self,server_ip,server_port):
        try:
            self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.server_address = (server_ip,server_port)
        finally:
            self.socket.close()
    def send(self,message):
        try:
            self.socket.connect(self.server_address)
            msg_encode = json.dumps(message)
            sock.sendall(bytes(msg_encode,encoding="utf-8"))
        finally:
            self.socket.close()
        
