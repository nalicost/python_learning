"""
                    共享内存演示
"""
from multiprocessing import Process, Value, Array
money = Value('i', 5000)


def worker_a(mon):
    mon.value += 1000


def worker_b(mon):
    mon.value -= 800


mon_a, mon_b = Process(target=worker_a, args=(money,)), Process(target=worker_b, args=(money, ))
if __name__ == '__main__':
    mon_a.start()
    mon_b.start()
    mon_a.join()
    mon_b.join()
    print(money.value)


list_ = Array('i', [1, 2, 3, 4])
list_a = Array('c', b'hello')


def worker_c(list_target):
    for i in list_target:
        print(i)
    list_target[1] = 1000


def worker_d(str_target):
    for i in str_target:
        print(i)
    str_target[1] = b'H'


num = Process(target=worker_c, args=(list_,))
num_a = Process(target=worker_d, args=(list_a, ))
if __name__ == '__main__':
    num.start()
    num_a.start()
    num_a.join()
    num.join()
    for i in list_:
        print(i)
    print(list_a.value)

# 在linux中不需要传入参数，由于使用fork，会将Pipe对象完全复制，故可以互相通信，但是在windows中，由于是通过导入模块实现，故子进程运行时会再次生
# 成Pipe对象，但父进程与各子进程的Pipe对象是不同的，故无法互相通信
