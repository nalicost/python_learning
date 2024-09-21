"""
                        队列通信演示
"""
from multiprocessing import Queue, Process
from random import randint
from time import sleep
queue = Queue()


def worker_a(q):
    for i in range(6):
        q.put(randint(1,33))
    q.put(randint(1, 16))


def worker_b(q):
    while True:
        # print('摇啊摇....')
        sleep(1)
        try:
            print(q.get(timeout=3), end=' ')
        except:
            break


a, b = Process(target=worker_a, args=(queue,)), Process(target=worker_b, args=(queue,))
if __name__ == '__main__':
    a.start()
    b.start()
    a.join()
    b.join()

# 在linux中不需要传入参数，由于使用fork，会将Pipe对象完全复制，故可以互相通信，但是在windows中，由于是通过导入模块实现，故子进程运行时会再次生
# 成Pipe对象，但父进程与各子进程的Pipe对象是不同的，故无法互相通信
