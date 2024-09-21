"""
                        tcp文件传输客户端
"""
import socket
import os
sockFD = socket.socket()
sockFD.connect(('127.0.0.1', 10086))
file_open = input('file name:>')
if os.path.exists(file_open):
    file_new_name = input('new file name:>')
    sockFD.send(file_new_name.encode())
    print(sockFD.recv(1024).decode())
    file_transport = open(file_open, 'rb')
    for data in file_transport:
        sockFD.send(data)
    sockFD.close()
