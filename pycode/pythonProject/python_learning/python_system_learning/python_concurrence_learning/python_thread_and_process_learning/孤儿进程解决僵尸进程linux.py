"""
                  创建二级子进程（配合wait）解决僵尸进程(linux)
"""
import time
import os


def a():
    time.sleep(5)
    print('写代码')


def b():
    time.sleep(3)
    print('测代码')


pid = os.fork()
if pid == 0:
    pid = os.fork()
    if pid > 0:
        os._exit(0)
    elif pid == 0:
        b()
elif pid > 0:
    a()
