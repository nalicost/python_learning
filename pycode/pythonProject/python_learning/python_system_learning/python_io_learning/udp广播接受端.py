"""
                    udp广播接受
"""
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind(('0.0.0.0', 9999))
while True:
    msg, addr = s.recvfrom(1024)
    print(msg.decode())
