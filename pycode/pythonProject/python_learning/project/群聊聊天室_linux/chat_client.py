# -*- encoding:gbk -*-
"""
                            聊天群客户端_linux
"""
import socket
import signal
import os
ADDR = ('192.168.233.1', 10086)
NAME = None


def add_chat(s):
    """
                加入申请
    :param s: 客户端使用的套接字
    """
    while True:
        global NAME
        NAME = input('你的姓名是：')
        msg = 'L ' + f'{NAME}'
        s.sendto(msg.encode(), ADDR)
        data, addr = s.recvfrom(128)
        if data.decode() == 'True':
            break
        else:
            print('名字重复')


def new_fork_creator(s):
    """
                进程创建
    :param s: 客户端使用的套接字
    """
    while True:
        data, addr = s.recvfrom(1024)
        print(data.decode(), end='')
        signal.signal(signal.SIGCHLD, signal.SIG_IGN)
        pid = os.fork()
        if pid < 0:
            print('进程创建失败')
        elif pid == 0:
            send_to(s)
        else:
            recv_(s)


def recv_(s):
    """
                接取消息
    :param s: 客户端使用的套接字
    """
    while True:
        data, addr = s.recvfrom(1024)
        if data.decode() == 'END':
            break
        print(data.decode(), end='')


def send_to(s):
    """
                发送消息
        :param s: 客户端使用的套接字
        """
    while True:
        msg = input('发送信息：')
        if msg == 'quit':
            s.sendto(f'Q {NAME}'.encode(), ADDR)
            break
        msg_pack = f'C {NAME} {msg}'
        s.sendto(msg_pack.encode(), ADDR)


def main():
    """
                客户端入口
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    add_chat(s)
    new_fork_creator(s)


main()
