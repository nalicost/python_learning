"""
                    基于gevent的tcp连接
"""
import gevent
from gevent import monkey
monkey.patch_all()
import socket


def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            c.close()
            return
        c.send(b'OK')


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('localhost', 10086))
s.listen(5)
while True:
    conn, addr = s.accept()
    print('Got connection from', addr)
    gevent.spawn(handle, conn)
