# -*-encoding:gbk -*-
"""
                    ͨ���źţ�signalģ�飩����ʬ����
"""
import time
import os
import signal


def a():
    time.sleep(5)
    print('д����')


def b():
    time.sleep(3)
    print('�����')


signal.signal(signal.SIGCHLD, signal.SIG_IGN)
pid = os.fork()
if pid == 0:
    b()
elif pid > 0:
    a()
