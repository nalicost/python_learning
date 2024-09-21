"""
                管道进程通信演示
"""
from multiprocessing import Pipe, Process
fd1, fd2 = Pipe()


# windows中
def worker_a(fd):
    print('启动程序a')
    print('请求b应用权限')
    fd.send('请求权限')
    data = fd.recv()
    if data:
        print('登录成功', data)


def worker_b(fd):
    data = fd.recv()
    print(data)
    fd.send('Dava')


a = Process(target=worker_a, args=(fd1, ))
b = Process(target=worker_b, args=(fd2, ))
if __name__ == '__main__':
    a.start()
    b.start()
    a.join()
    b.join()


# 在linux中不需要传入参数，由于使用fork，会将Pipe对象完全复制，故可以互相通信，但是在windows中，由于是通过导入模块实现，故子进程运行时会再次生
# 成Pipe对象，但父进程与各子进程的Pipe对象是不同的，故无法互相通信
