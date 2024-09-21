"""
            greenlet第三方模块实现协程
"""
import greenlet


def worker_a():
    print('start worker a')
    gr2.switch()
    print('worker a finished')
    gr2.switch()


def worker_b():
    print('start worker b')
    gr1.switch()
    print('worker b finished')


gr1 = greenlet.greenlet(worker_a)
gr2 = greenlet.greenlet(worker_b)
gr1.switch()
