"""
                生成器练习
"""
list_01 = [2, 3, 4, 5, 6, 7]
list_02 = []
list_03 = [10, 5]
# 第一种实现方式，用列表已定义好的生成器方式即__iter__，通过for的第一步自动生成生成器（也是迭代器本身）{具体过程为使用yield语法，先生成一个生成
# 器类，并将yield以上与上次循环yield以下的代码放入__next__中，并以yield后面的内容为函数返回值，作为列表这一数据框架拿出数据的迭代方式}，然后通
# 过for的第二步调用对应的生成器中的__next__函数来以已定义好的方式从数据框架中拿出数据
# for item in list_01:
#     if item % 2 == 0:
#         list_02.append(item)
# print(list_02)
# 第二种实现方式，自己定义生成器


def get_list_even_number(target_list):
    begin = 0
    while begin < len(target_list):
        if target_list[begin] % 2 == 0:
            yield target_list[begin]
        begin += 1


my01 = get_list_even_number(list_01)
for item in my01:
    list_02.append(item)
print(list_02)
"""
            生成器源码
    class MyGenerator:
        def __init__(self):
            pass

        def __iter__(self):
            return self

        def __next__(self):
            pass
"""
# 练习：使用生成器以元组返回列表元素索引值


def my_enumerate(iterable_object):
    num = 0
    while num < len(iterable_object):
        yield num, num
        num += 1


me = my_enumerate(list_01)
for item in me:
    print(item)
# 练习：使用生成器以元组形式合并两个列表


def my_zip(*args):
    """
            列表合并器
    :param args: iterable object
    :return: tuple
    """
    num = 0
    while True:
        result = []
        try:
            for item01 in args:
                result.append(item01[num])
        except IndexError:
            break
            # 如果raise StopInteration，会使起产生RunTimeError
            # 同时出现yield生成器函数，无法return
            # 二者的原因都是在于生成器函数退出时，由于没有yield为next提供新的函数代码，所以next直接抛出StopInteration，故返回值无法返回，同
            # 时如果退出生成器时因为StopInteration，相当于同时抛出两个相同的故报RunTimeError错误
            # 对自动抛出StopInteration的猜测，是由于当使用生成器生成生成器类是其中next会继承父类中的raise StopInteration，如果yield未对
            # 生成器重写，那么就会使用父类的方法
        yield tuple(result)
        num += 1


for item in my_zip(list_01, list_03, [1, 2, 5, 10]):
    print(item)
