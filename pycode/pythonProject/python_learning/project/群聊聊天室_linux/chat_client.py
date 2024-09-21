# -*- encoding:gbk -*-
"""
                            ����Ⱥ�ͻ���_linux
"""
import socket
import signal
import os
ADDR = ('192.168.233.1', 10086)
NAME = None


def add_chat(s):
    """
                ��������
    :param s: �ͻ���ʹ�õ��׽���
    """
    while True:
        global NAME
        NAME = input('��������ǣ�')
        msg = 'L ' + f'{NAME}'
        s.sendto(msg.encode(), ADDR)
        data, addr = s.recvfrom(128)
        if data.decode() == 'True':
            break
        else:
            print('�����ظ�')


def new_fork_creator(s):
    """
                ���̴���
    :param s: �ͻ���ʹ�õ��׽���
    """
    while True:
        data, addr = s.recvfrom(1024)
        print(data.decode(), end='')
        signal.signal(signal.SIGCHLD, signal.SIG_IGN)
        pid = os.fork()
        if pid < 0:
            print('���̴���ʧ��')
        elif pid == 0:
            send_to(s)
        else:
            recv_(s)


def recv_(s):
    """
                ��ȡ��Ϣ
    :param s: �ͻ���ʹ�õ��׽���
    """
    while True:
        data, addr = s.recvfrom(1024)
        if data.decode() == 'END':
            break
        print(data.decode(), end='')


def send_to(s):
    """
                ������Ϣ
        :param s: �ͻ���ʹ�õ��׽���
        """
    while True:
        msg = input('������Ϣ��')
        if msg == 'quit':
            s.sendto(f'Q {NAME}'.encode(), ADDR)
            break
        msg_pack = f'C {NAME} {msg}'
        s.sendto(msg_pack.encode(), ADDR)


def main():
    """
                �ͻ������
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    add_chat(s)
    new_fork_creator(s)


main()
