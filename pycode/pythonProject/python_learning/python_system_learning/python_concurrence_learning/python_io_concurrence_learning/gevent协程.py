"""
            gevent实现协程
"""
import gevent
from gevent import monkey
monkey.patch_all()
from time import sleep


def worker_a(a, b):
    print('worker_a start ', a, b)
    sleep(2)
    print('worker_a end ', a, b)


def worker_b():
    print('worker_b start')
    sleep(3)
    print('worker_b end')


a = gevent.spawn(worker_a, 10, 5)
b = gevent.spawn(worker_b)
gevent.joinall([a, b])
