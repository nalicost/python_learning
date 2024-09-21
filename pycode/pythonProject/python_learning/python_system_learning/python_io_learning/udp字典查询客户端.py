"""
                        基于udp的字典查询客户端
"""
import socket
ADDR = ('127.0.0.1', 10086)
sockFD = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    msg = input('查询的单词是:>')
    if not msg:
        break
    sockFD.sendto(msg.encode(), ADDR)
    data, addr = sockFD.recvfrom(1024)
    print(data.decode())
sockFD.close()
