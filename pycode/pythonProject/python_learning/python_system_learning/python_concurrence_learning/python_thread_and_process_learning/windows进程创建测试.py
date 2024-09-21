# -*- encoding:gbk -*-
"""
                父子进程关系(windows)
"""
import multiprocessing
import time
import os


def a(msg):
    for i in range(3):
        print(f'process 1 {msg}', '子：', os.getpid(), '父：', os.getppid())
        time.sleep(1)


p1 = multiprocessing.Process(target=a, args='A')
p2 = multiprocessing.Process(target=a, args='B')
if __name__ == '__main__':
    print(os.getpid())
    p1.start()
    p2.start()
