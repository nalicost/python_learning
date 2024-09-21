"""
                    lock实现线程间互斥
"""
import threading
from threading import Lock
from time import sleep
lock = Lock()


def worker_a():
    print('worker_a started')
    lock.acquire()
    sleep(4)
    print('worker_a finished')
    lock.release()


t1 = threading.Thread(target=worker_a)
t1.start()
sleep(3)
lock.acquire()
print('main thread started')
lock.release()
print('main thread finished')
t1.join()
