"""
                        设置超时检测的套接字
"""
from socket import *
ADDR = ('127.0.0.1', 10086)
sock = socket()
sock.bind(ADDR)
sock.listen(5)
sock.settimeout(3)
while True:
    try:
        conn, addr = sock.accept()
        print('Connected', addr)
    except timeout:
        print('没有人')
