# -*- encoding:gbk -*-
"""
                            ����Ⱥ�����_linux
"""
import socket
import signal
import os
USER_DICT, ADDR = {}, ('192.168.16.130', 10086)


def administrator_msg(sock):
    """
                ����Ա��Ϣ����
    :param sock: �ͻ���ʹ�õ��׽���
    """
    while True:
        msg = input('����Ա֪ͨ:>')
        if msg == 'exit':
            break
        msg_pack = f'C ����Ա {msg}'
        sock.sendto(msg_pack.encode(), ADDR)


def user_choice(list_, msg_send, sock):
    """
                ѡ���û�������Ϣ
    :param list_: �û������б�
    :param msg_send: ��Ҫ���͵���Ϣ
    :param sock: �����ʹ�õ��׽���
    """
    for user in USER_DICT:
        if user != list_[1]:
            sock.sendto(msg_send.encode(), USER_DICT[user])


def log(sock, list_, addr_):
    """
                ��¼������
    :param sock: �����ʹ�õ��׽���
    :param list_: �û������б�
    :param addr_:  �û���ַ
    """
    if list_[1] not in USER_DICT and '����Ա' not in list_[1]:
        USER_DICT[list_[1]] = addr_
        sock.sendto(b'True', addr_)
        msg = f"\n��ӭ'{list_[1]}'����������\n������Ϣ��"
        user_choice(list_, msg, sock)
        sock.sendto('��ӭ����Ⱥ��\n'.encode(), addr_)
    else:
        sock.sendto(b'False', addr_)


def send_msg(sock, list_):
    """
                ѡ���û�������Ϣ
    :param list_: �û������б�
    :param sock: �����ʹ�õ��׽���
    """
    msg_merge = ' '.join(list_[2:])
    msg_send = f'\n{list_[1]}��{msg_merge}\n������Ϣ��'
    user_choice(list_, msg_send, sock)


def leave(sock, list_):
    """
                ѡ���û�������Ϣ
    :param list_: �û������б�
    :param sock: �����ʹ�õ��׽���
    """
    msg = f"\n'{list_[1]}'�˳�Ⱥ��\n������Ϣ��"
    user_choice(list_, msg, sock)
    sock.sendto(b'END', USER_DICT[list_[1]])
    del USER_DICT[list_[1]]


def main():
    """
                ����������
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(ADDR)
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)
    pid = os.fork()
    if pid < 0:
        print('���̴���ʧ��')
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
