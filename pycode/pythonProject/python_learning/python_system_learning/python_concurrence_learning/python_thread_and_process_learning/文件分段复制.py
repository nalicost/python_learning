# -*-encoding:gbk -*-
"""
                    文件双进程复制
"""
import os
from multiprocessing import *


def worker(file_open_name, len_start, len_end, file_num):
    file_name = f'{file_num}' + file_open_name
    with open(file_name, 'wb') as f_new:
        with open(file_open_name, 'rb') as f_old:
            # 一定要在进程内部开启，否则可能倒置文件提前关闭
            f_old.seek(len_start)
            while f_old.tell() < len_end:
                f_new.write(f_old.read(1))


if __name__ == '__main__':
    file_name_old = input('文件名字是:>')
    len_target = os.path.getsize(file_name_old)
    p1 = Process(target=worker, args=(file_name_old, 0, len_target // 2, 1))
    p2 = Process(target=worker, args=(file_name_old, len_target // 2, len_target, 2))
    # 由于类似当时的链表，当光标指到的位置，已经写完了，每次写是写下一个，故p2起始为半个文件处
    p1.start()
    p2.start()

"""
import os
from multiprocessing import *


def worker(f_old, len_start, len_end, file_num):
    file_name = f'{file_num}' + f_old.name
    with open(file_name, 'wb') as f_new:
        f_old.seek(len_start)
        while f_old.tell() < len_end:
            f_new.write(f_old.read(1))


file_name_old = input('文件名字是:>')
len_target = os.path.getsize(file_name_old)
with open(file_name_old, 'rb') as file_old:
    p1 = Process(target=worker, args=(file_old, 0, len_target//2, 1))
    p2 = Process(target=worker, args=(file_old, len_target//2, len_target, 2))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    # 或者可以通过父进程等待子进程结束来防止文件由于父进程结束提前销毁，即将join写在with语句块内部 
"""