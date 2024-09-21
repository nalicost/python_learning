"""
                    套接字客户端使用流程熟悉
"""
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 10086))
while True:
    msg = input('message:>')
    if msg == 'quit':
        break
    sock.send(msg.encode())
    data = sock.recv(1024)
    print(data.decode())
sock.close()
