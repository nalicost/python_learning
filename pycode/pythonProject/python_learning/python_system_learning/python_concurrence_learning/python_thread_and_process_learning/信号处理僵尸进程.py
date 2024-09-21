# -*-encoding:gbk -*-
"""
                    通过信号（signal模块）处理僵尸进程
"""
import time
import os
import signal


def a():
    time.sleep(5)
    print('写代码')


def b():
    time.sleep(3)
    print('测代码')


signal.signal(signal.SIGCHLD, signal.SIG_IGN)
pid = os.fork()
if pid == 0:
    b()
elif pid > 0:
    a()
