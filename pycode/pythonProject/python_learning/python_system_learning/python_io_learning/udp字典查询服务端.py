"""
                    基于udp的字典查询服务端
"""
import socket
from 字典中查找单词 import *
sockFD = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sockFD.bind(('localhost', 10086))
while True:
    data, addr = sockFD.recvfrom(1024)
    sockFD.sendto(seek_word(data.decode()).encode(), addr)
