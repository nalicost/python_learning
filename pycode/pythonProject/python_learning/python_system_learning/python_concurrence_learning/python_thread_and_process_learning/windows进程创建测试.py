# -*- encoding:gbk -*-
"""
                ���ӽ��̹�ϵ(windows)
"""
import multiprocessing
import time
import os


def a(msg):
    for i in range(3):
        print(f'process 1 {msg}', '�ӣ�', os.getpid(), '����', os.getppid())
        time.sleep(1)


p1 = multiprocessing.Process(target=a, args='A')
p2 = multiprocessing.Process(target=a, args='B')
if __name__ == '__main__':
    print(os.getpid())
    p1.start()
    p2.start()
