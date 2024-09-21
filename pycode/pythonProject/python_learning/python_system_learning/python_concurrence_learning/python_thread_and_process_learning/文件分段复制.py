# -*-encoding:gbk -*-
"""
                    �ļ�˫���̸���
"""
import os
from multiprocessing import *


def worker(file_open_name, len_start, len_end, file_num):
    file_name = f'{file_num}' + file_open_name
    with open(file_name, 'wb') as f_new:
        with open(file_open_name, 'rb') as f_old:
            # һ��Ҫ�ڽ����ڲ�������������ܵ����ļ���ǰ�ر�
            f_old.seek(len_start)
            while f_old.tell() < len_end:
                f_new.write(f_old.read(1))


if __name__ == '__main__':
    file_name_old = input('�ļ�������:>')
    len_target = os.path.getsize(file_name_old)
    p1 = Process(target=worker, args=(file_name_old, 0, len_target // 2, 1))
    p2 = Process(target=worker, args=(file_name_old, len_target // 2, len_target, 2))
    # �������Ƶ�ʱ�����������ָ����λ�ã��Ѿ�д���ˣ�ÿ��д��д��һ������p2��ʼΪ����ļ���
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


file_name_old = input('�ļ�������:>')
len_target = os.path.getsize(file_name_old)
with open(file_name_old, 'rb') as file_old:
    p1 = Process(target=worker, args=(file_old, 0, len_target//2, 1))
    p2 = Process(target=worker, args=(file_old, len_target//2, len_target, 2))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    # ���߿���ͨ�������̵ȴ��ӽ��̽�������ֹ�ļ����ڸ����̽�����ǰ���٣�����joinд��with�����ڲ� 
"""