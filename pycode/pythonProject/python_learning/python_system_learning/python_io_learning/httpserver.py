"""
                熟悉http请求与响应格式练习
"""
from socket import *


def request(conn_recv):
    if not conn_recv:
        return "HTTP/1.1 404 NOT FOUND A\n\r\n\rsorry"
    list_conn = conn_recv.decode().split(' ')
    if list_conn[1] == '/':
        file_need = open('index.html', 'r')
        return "HTTP/1.1 200 OK\n\r\n\r" + file_need.read()
    else:
        return "HTTP/1.1 404 NOT FOUND\n\r\n\rsorry"


sockFD = socket()
sockFD.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sockFD.bind(('192.168.137.1', 10086))
sockFD.listen(3)
while True:
    conn, addr = sockFD.accept()
    rq = conn.recv(4096)
    print('recv msg:', rq.decode(), '#')
    re = request(rq)
    conn.send(re.encode())
