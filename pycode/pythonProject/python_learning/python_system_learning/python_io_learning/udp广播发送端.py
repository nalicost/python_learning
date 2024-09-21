"""
            udp广播发送
"""
import socket
import time
destination = ('192.168.16.255', 9999)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
data = b'hello world'
while True:
    time.sleep(2)
    s.sendto(data, destination)
