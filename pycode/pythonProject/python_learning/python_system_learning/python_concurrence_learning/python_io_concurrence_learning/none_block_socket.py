"""
                    设置无阻塞的套接字
"""
from socket import *
ADDR = ('127.0.0.1', 10086)
sock = socket(AF_INET, SOCK_STREAM)
sock.bind(ADDR)
sock.listen(5)
sock.setblocking(False)
while True:
    try:
        conn, addr = sock.accept()
        print('Connected by', addr)
    except BlockingIOError:
        print('没有人')
