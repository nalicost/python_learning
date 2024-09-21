"""
                                    测试线程进程的效率
"""
import time
from multiprocessing import Process
from threading import Thread


def time_calculator(fun_old):
    def wrapper(*args, **kwargs):
        start_ = time.time()
        fun_old(*args, **kwargs)
        end_ = time.time()
        print(end_ - start_, 'second')

    return wrapper


def repeat_worker(fun_old):
    @time_calculator
    def wrapper(*args, **kwargs):
        for i_ in range(10):
            fun_old(*args, **kwargs)

    return wrapper


# @repeat_worker
def worker_calculate(x, y):
    c = 0
    while c < 7000000:
        x += 1
        y += 1
        c += 1


# @repeat_worker
def worker_io():
    with open('test_efficiency.txt', 'w') as f:
        for i_ in range(1800000):
            f.write('hello world\n')
    with open('test_efficiency.txt', 'r') as f:
        f.readlines()


if __name__ == '__main__':
    # worker_io()
    # worker_calculate(0, 0)
    list_ = []
    start = time.time()
    for i in range(10):
        p = Process(target=worker_io)
        list_.append(p)
        p.start()
    for i in list_:
        i.join()
    end = time.time()
    print(end - start, 'second')
    list_ = []
    start = time.time()
    for i in range(10):
        q = Process(target=worker_calculate, args=(0, 0))
        list_.append(q)
        q.start()
    for i in list_:
        i.join()
    end = time.time()
    print(end - start, 'second')
    list_ = []
    start = time.time()
    for i in range(10):
        p = Thread(target=worker_io)
        list_.append(p)
        p.start()
    for i in list_:
        i.join()
    end = time.time()
    print(end - start, 'second')
    list_ = []
    start = time.time()
    for i in range(10):
        q = Thread(target=worker_calculate, args=(0, 0))
        list_.append(q)
        q.start()
    for i in list_:
        i.join()
    end = time.time()
    print(end - start, 'second')
