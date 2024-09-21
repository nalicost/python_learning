"""
                                线程（thread）练习
"""
from threading import Thread
from time import sleep


class MyThread(Thread):
    def __init__(self, func_name, args, kwargs):
        super().__init__()
        self.func_name = func_name
        self.args = args
        self.kwargs = kwargs

    def run(self):
        self.func_name(*self.args, **self.kwargs)


def player(sec, song):
    for i in range(3):
        print(f'{song} is playing')
        sleep(sec)


mt = MyThread(player, (3, ), {'song': '凉凉'})
mt.start()
mt.join()
