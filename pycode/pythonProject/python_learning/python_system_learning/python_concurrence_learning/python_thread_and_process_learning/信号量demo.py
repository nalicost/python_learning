"""
                    信号量演示
"""
from multiprocessing import Semaphore, Process
from time import sleep
sem = Semaphore(3)


def worker(id_, sem_):
    sem_.acquire()
    print(f'执行中{id_}')
    sleep(3)
    sem_.release()


if __name__ == '__main__':
    list_process = []
    for i in range(10):
        p = Process(target=worker, args=(i, sem))
        list_process.append(p)
        p.start()
    for i in list_process:
        i.join()


# 在linux中不需要传入参数，由于使用fork，会将Pipe对象完全复制，故可以互相通信，但是在windows中，由于是通过导入模块实现，故子进程运行时会再次生
# 成Pipe对象，但父进程与各子进程的Pipe对象是不同的，故无法互相通信
