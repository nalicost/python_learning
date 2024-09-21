"""
                    udp套接字客户端流程
"""
import socket
ADDR = ('127.0.0.1', 10086)
sockFD = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    msg = input("message:>")
    if not msg:
        break
    sockFD.sendto(msg.encode(), ADDR)
    data, addr = sockFD.recvfrom(1024)
    print(addr, data.decode())
sockFD.close()
