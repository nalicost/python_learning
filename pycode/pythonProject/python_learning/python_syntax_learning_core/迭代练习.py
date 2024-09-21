"""
                关于for的迭代器原理练习
"""
# 练习一：('铁扇公主', '铁锤公主', '扳手王子')用迭代器原理实现for的遍历
a_tuple = ('铁扇公主', '铁锤公主', '扳手王子')
iter_a_tuple = a_tuple.__iter__()
while True:
    try:
        elements = iter_a_tuple.__next__()
        print(elements)
    except StopIteration:
        break
# 练习二：{'铁扇公主'： 101, '铁锤公主'： 102, '扳手王子'： 103}用迭代器原理实现for的遍历
a_dict = {'铁扇公主': 101, '铁锤公主': 102, '扳手王子': 103}
a_dict_iter = a_dict.__iter__()
while True:
    try:
        element01 = a_dict_iter.__next__()
        print(element01, a_dict[element01])
    except StopIteration:
        break
# 练习三：自制迭代器


class GraphicManager:
    def __init__(self):
        self.__shapes_list = []

    def calculate_total_area(self):
        pass

    def add_shape(self, graphic):
        self.__shapes_list.append(graphic)

    def __iter__(self):
        return GraphicIterator(self.__shapes_list)


class GraphicIterator:
    def __init__(self, target):
        # 封装了要迭代的对象与迭代的位置
        self.__target = target
        self.__index = -1

    def __next__(self):
        self.__index += 1
        if self.__index >= len(self.__target):
            raise StopIteration
        return self.__target[self.__index]


class Graphic:
    pass


object_01 = GraphicManager()
object_01.add_shape(Graphic())
object_01.add_shape(Graphic())
object_01.add_shape(Graphic())
for item in object_01:
    print(item)
