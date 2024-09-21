"""
                udp套接字服务端流程
"""
import socket
sockFD = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sockFD.bind(('127.0.0.1', 10086))
while True:
    msg, addr = sockFD.recvfrom(1024)
    print(msg.decode())
    sockFD.sendto(b'thanks', addr)
