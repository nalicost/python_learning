"""
                迭代器的运用
"""


class MyRange:
    def __init__(self, end_num):
        self.__end_num = end_num

    def __iter__(self):
        return MyRangeIterator(self.__end_num)


class MyRangeIterator:
    def __init__(self, target):
        self.__target = target
        self.__begin = -1

    def __next__(self):
        self.__begin += 1
        if self.__begin >= self.__target:
            raise StopIteration
        return self.__begin


for item in MyRange(10):
    print(item)
