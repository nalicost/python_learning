# -*- encoding:gbk -*-
"""
                            聊天群服务端_linux
"""
import socket
import signal
import os
USER_DICT, ADDR = {}, ('192.168.16.130', 10086)


def administrator_msg(sock):
    """
                管理员消息发送
    :param sock: 客户端使用的套接字
    """
    while True:
        msg = input('管理员通知:>')
        if msg == 'exit':
            break
        msg_pack = f'C 管理员 {msg}'
        sock.sendto(msg_pack.encode(), ADDR)


def user_choice(list_, msg_send, sock):
    """
                选择用户发送信息
    :param list_: 用户请求列表
    :param msg_send: 需要发送的信息
    :param sock: 服务端使用的套接字
    """
    for user in USER_DICT:
        if user != list_[1]:
            sock.sendto(msg_send.encode(), USER_DICT[user])


def log(sock, list_, addr_):
    """
                登录请求处理
    :param sock: 服务端使用的套接字
    :param list_: 用户请求列表
    :param addr_:  用户地址
    """
    if list_[1] not in USER_DICT and '管理员' not in list_[1]:
        USER_DICT[list_[1]] = addr_
        sock.sendto(b'True', addr_)
        msg = f"\n欢迎'{list_[1]}'加入聊天室\n发送信息："
        user_choice(list_, msg, sock)
        sock.sendto('欢迎加入群聊\n'.encode(), addr_)
    else:
        sock.sendto(b'False', addr_)


def send_msg(sock, list_):
    """
                选择用户发送信息
    :param list_: 用户请求列表
    :param sock: 服务端使用的套接字
    """
    msg_merge = ' '.join(list_[2:])
    msg_send = f'\n{list_[1]}：{msg_merge}\n发送消息：'
    user_choice(list_, msg_send, sock)


def leave(sock, list_):
    """
                选择用户发送信息
    :param list_: 用户请求列表
    :param sock: 服务端使用的套接字
    """
    msg = f"\n'{list_[1]}'退出群聊\n发送消息："
    user_choice(list_, msg, sock)
    sock.sendto(b'END', USER_DICT[list_[1]])
    del USER_DICT[list_[1]]


def main():
    """
                服务端主入口
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(ADDR)
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)
    pid = os.fork()
    if pid < 0:
        print('进程创建失败')
    elif pid == 0:
        while True:
            data, addr = s.recvfrom(1024)
            msg_list = data.decode().split(' ')
            if msg_list[0] == 'L':
                log(s, msg_list, addr)
            elif msg_list[0] == 'C':
                send_msg(s, msg_list)
            elif msg_list[0] == 'Q':
                leave(s, msg_list)
    else:
        administrator_msg(s)


main()
