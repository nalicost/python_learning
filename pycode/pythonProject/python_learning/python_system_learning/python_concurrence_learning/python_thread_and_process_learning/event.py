"""
                event实现线程间互斥
"""
import threading
from threading import Event
e = Event()


def worker_a():
    print('worker a started')
    e.wait()
    e.clear()
    print('worker a finished')
    e.set()


def worker_b():
    print('worker b started')
    e.wait()
    e.clear()
    print('worker b finished')
    e.set()


t1 = threading.Thread(target=worker_a)
t2 = threading.Thread(target=worker_b)
t1.start()
t2.start()
e.set()
t1.join()
t2.join()
