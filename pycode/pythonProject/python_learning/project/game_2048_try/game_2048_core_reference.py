"""
                                  本代码为参考答案，只有核心代码
                                  虽然不使用传参而使用全局变量有些许麻烦
                                  但是很好的练习了局部变量，全局变量与切片内存图，
                                  还有删除原理等一系列内容，值得以后好好品味
"""
map = [
    [8, 0, 0, 0],
    [4, 0, 4, 0],
    [4, 2, 0, 0],
    [2, 0, 8, 16]
]
list_merge = None

def zero_to_end():
    for i in range(-1,-len(list_merge),-1):
        if list_merge[i] == 0:
            del list_merge[i]
            list_merge.append(0)


def merge():
    zero_to_end()
    for i in range(len(list_merge)-1):
        if list_merge[i] == list_merge[i+1]:
            list_merge[i] += list_merge[i+1]
            del list_merge[i+1]
            list_merge.append(0)


def move_left():
    for line in map:
        global list_merge
        # 必须加global，由于该函数调用其他函数时，其他函数会生成自己的栈帧，是互相独立的所以寻找变量时往外寻找的不是move_left里的局部变量而是
        # 全局变量，所以想要使其他函数接受list_merge就必须直接修改全局变量
        list_merge = line
        merge()


def move_right():
    for line in map:
        global list_merge
        list_merge = line[::-1]
        # 注意由于切边取出是生成新的列表，故list_merge的修改不影响line，没人接受，map也不会修改
        merge()
        line[::-1] = list_merge
        # 所以这里使line倒着赋予新的值，使其能够接受，达成效果


def move_up():
    square_transform(map)
    move_left()
    square_transform(map)


def move_down():
    square_transform(map)
    move_right()
    square_transform(map)


def square_transform(list_target):
    # 通过将二维列表的外层索引和内层索引化为坐标，并将坐标互换，来达到纵列交换的效果
    """
                矩阵转换
    :param list_target: 所移动的对象列表
    """
    for i in range(1, len(list_target)):
        for k in range(0, i):
            list_target[i][k], list_target[k][i] = list_target[k][i], list_target[i][k]
