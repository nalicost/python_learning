"""
                      2048游戏核心算法及在命令行游玩的简单方式
"""
import random
import copy


def list_lmove(list_target):
    # 移动通过将所有的0放至右侧其他元素顺序不变达成
    """
                列表左移
    :param list_target: 所移动的对象列表
    """
    for i in range(len(list_target) - 1):
        for j in range(len(list_target) - 1):
            if list_target[j] == 0:
                # 是0就与右侧的数据交换
                list_target[j], list_target[j+1] = list_target[j+1], list_target[j]
    list_sum_same(list_target)


def list_rmove(list_target):
    # 将列表反转，左移，再反转，达到右移的效果
    """
                列表右移
    :param list_target: 所移动的对象列表
    """
    list_target.reverse()
    list_lmove(list_target)
    list_sum_same(list_target)
    list_target.reverse()


def list_abmove(list_target):
    # 将列表先进行矩阵转换后，左移，然后再矩阵转换，来实现上移的效果
    """
                 列表上移
    :param list_target: 所移动的对象列表
    """
    square_transform(list_target)
    list_lmove_all(list_target)
    square_transform(list_target)


def list_lomove(list_target):
    # 将列表进行矩阵转换后，右移，然后再矩阵转换，来实现下移的效果
    """
                 列表下移
    :param list_target: 所移动的对象列表
    """
    square_transform(list_target)
    list_rmove_all(list_target)
    square_transform(list_target)


def square_transform(list_target):
    # 通过将二维列表的外层索引和内层索引化为坐标，并将坐标互换，来达到纵列交换的效果
    """
                矩阵转换
    :param list_target: 所移动的对象列表
    """
    for i in range(1, len(list_target)):
        for k in range(0, i):
            list_target[i][k], list_target[k][i] = list_target[k][i], list_target[i][k]


def list_sum_same(list_target):
    # 通过将相邻的相同从左到右依次加和，循环结束的条件为0的数量不变，由于加和一次多一个0
    """
                合并同类
    :param list_target: 所移动的对象列表
    """
    zero_num = list_target.count(0) + 1
    while list_target.count(0) != zero_num:
        zero_num = list_target.count(0)
        for i in range(len(list_target) - 1):
            if list_target[i] == list_target[i + 1]:
                list_target[i + 1] = list_target[i + 1] * 2
                del list_target[i]
                # remove不要随便用，只删范围内靠左的第一个
                list_target.append(0)


def list_lmove_all(list_target):
    """

    :param list_target:
    """
    for i in list_target:
        list_lmove(i)


def list_rmove_all(list_target):
    """

    :param list_target:
    """
    for i in list_target:
        list_rmove(i)


def is_continue(list_target):
    """
                游戏结束判断
    :param list_target: 所判断的对象列表
    :return: bool
    """
    list_target = copy.deepcopy(list_target)
    list_abmove(list_target)
    list_lomove(list_target)
    list_rmove_all(list_target)
    list_lmove_all(list_target)
    # 将列表所有可能的情况都试一遍，只要0还存在说明游戏未结束
    for i in list_target:
        if 0 in i:
            return True
    return False


def print_game_situation(list_target):
    """
                    游戏当前进程打印
        :param list_target: 所判断的对象列表
    """
    for i in list_target:
        for j in i:
            print(f'{j}'.ljust(5, ' '), end=' ')
        print()
    print('-' * 25)


def isrestart(select):
    """
                游戏是否重启判断
    :param select: 需判断的对象
    """
    global game_list
    if select == 'r':
        game_list = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]


def random_num_produce(list_input, list_output):
    """
                二维列表随机数字生成器
    :param list_input: 可以生成随机数字的二维列表的位置
    :param list_output: 已放入随机数字的新的列表
    """
    x, y = random.sample(list_input, 1)[0]
    # 随机选择数字出现的格子
    add_list = [2] if count < 254 else [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4] if count < 512 else [2, 2, 2, 2, 4]
    # 当数字较大时，增加4出现的概率，减少游戏难度
    list_output[x][y] = random.sample(add_list, 1)[0]


def num_random_range_produce(list_input):
    """
                二维列表随机数字可生成位置生成器
    :param list_input: 需要生成随机数字的二维列表
    """
    for key in range(len(list_input)):
        for value in range(len(list_input)):
            if list_input[key][value] == 0:
                # 保证新生成的数字出现范围不会覆盖已有数字的格子
                game_list_info.append((key, value))
            sum_all_num(key, value, list_input)


def sum_all_num(key, value, list_input):
    """
                统计列表中所有数的和
    :param key: 需要查找二维列表的对应外层索引
    :param value: 需要查找二维列表的对应内层索引
    :param list_input: 需要查找的二维列表
    """
    if list_input[key][value] >= 128:
        # 计算大于等于128的数字个数
        global count
        count += list_input[key][value]


def select_func(select):
    """
                功能选择判断
    :param select: 需要判断的内容
    """
    if select in ('w', 'a', 's', 'd'):
        choice_dict[select](game_list)
        print_game_situation(game_list)
    elif select not in ('q', 'r'):
        print('请输入指定内容。')


game_list = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
game_list_backup = []
choice = None
choice_dict = {'w': list_abmove, 'a': list_lmove_all, 's': list_lomove, 'd': list_rmove_all}
while choice != 'q':
    game_list_info = []
    count = 0
    num_random_range_produce(game_list)
    if game_list_backup == game_list:
        # 如果移动前后无变化，说明无法移动
        print('无法移动')
    else:
        random_num_produce(game_list_info, game_list)
    print_game_situation(game_list)
    game_list_backup = copy.deepcopy(game_list)
    if is_continue(game_list_backup):
        choice = input('请输入wasd中的一个来进行上下左右移动,输入q退出，输入r重新开始>:')
        isrestart(choice)
        select_func(choice)
    else:
        choice = input('游戏结束，输入q退出或输入r重新开始>:')
        isrestart(choice)
