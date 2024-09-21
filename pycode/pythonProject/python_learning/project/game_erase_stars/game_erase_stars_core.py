"""
                        消除星星的核心代码，不会有实体，同时是面向对象的尝试
"""


class EraseStarsItem:
    """
            星星类
    """
    def __init__(self, colour,  location):
        """
                星星的数据成员
        :param colour: 颜色
        :param location: 位置
        """
        self.colour = colour
        self.location = location

    def close_count(self, target_list):
        """
                星星的相邻统计
        :param target_list: 查找列表
        :return: 输出所有相邻对象形成的集合
        """
        set_output ={self.colour, (self.location[0], self.location[1])}
        for k in (1, 0):
            for v in (0, 1):
                # 如果其坐标位置的右侧一个或下侧一个颜色相同，加进集合
                if self.colour == target_list[self.location[0] + k][self.location[1] + v]:
                    set_output.add((self.location[0] + k, self.location[1] + v))
        return set_output


def erase_stars_object_produce(target_list, output_list):
    """
            对象生成器
    :param target_list: 目标列表
    :param output_list: 输出列表
    """
    for k in range(len(target_list) - 2):
        for v in range(len(target_list[0]) - 2):
            item = EraseStarsItem(target_list[k + 1][v + 1], (k + 1 , v + 1))
            output_list.append(item)


def close_count_all(target_list, output_list):
    """
            相邻的所有数据整合
    :param target_list: 目标列表
    :param output_list: 输出列表
    """
    for item in target_list:
        # 将每一个对象相邻的集合放入大列表
        set_output = item.close_count(stars_game_situation)
        output_list.append(set_output)


def chain_of_stars(target_list):
    """
            将相邻的组成长链
    :param target_list: 操作列表
    """
    len_list = len(target_list) + 1
    while len(target_list) != len_list:
        # 检测是否所有相邻的对象都被整合进同一个大集合
        len_list = len(target_list)
        for k in range(-1, - len(target_list), -1):
            for v in range(k - 1, - len(target_list) - 1, -1):
                if len(target_list[k].intersection(target_list[v])) > 1:
                    # 依次取出后看交集长度是否大于1，大于代表有相同的对象，则判定这两个集合中的所有对象可以形成长链
                    target_list[k].update(target_list[v])
                    del target_list[v]
                    target_list.append({0})
                    # 保证列表长度不变，防止循环出错
    while {0} in target_list:
        target_list.remove({0})


def replace_0(target_list, output_list):
    """
            将符合条件的换为0
    :param target_list: 操作列表
    :param output_list: 输出列表
    """
    for k in range(len(target_list)):
        target_list[k] = list(target_list[k])
        for v in target_list[k]:
            if v in (1, 2, 3):
                target_list[k].remove(v)
        if len(target_list[k]) == 1:
            # 没有相邻的对象不变更颜色
            continue
        for i in range(len(target_list[k])):
            output_list[target_list[k][i][0]][target_list[k][i][1]] = 0


def zero_to_one(target_list):
    """
            左移
    :param target_list: 操作列表
    """
    for i in range(1, len(target_list) - 2):
        for j in range(1, len(target_list) - 2):
            if target_list[j] == 0:
                target_list[j], target_list[j+1] = target_list[j+1], target_list[j]


def square_transform(list_target):
    """
                矩阵转换
    :param list_target: 所移动的对象列表
    """
    for i in range(1, len(list_target)):
        for k in range(0, i):
            list_target[i][k], list_target[k][i] = list_target[k][i], list_target[i][k]


def lomove_all(list_target):
    """
            下移
    :param list_target: 移动的列表
    """
    square_transform(list_target)
    for line in list_target:
        line.reverse()
        zero_to_one(line)
        line.reverse()
    square_transform(list_target)


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


object_list = []
set_list = []
stars_game_situation = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 3, 1, 3, 2, 3, 0],
    [0, 1, 2, 3, 2, 2, 0],
    [0, 2, 2, 2, 2, 3, 0],
    [0, 3, 3, 3, 3, 3, 0],
    [0, 2, 2, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0]
    ]
erase_stars_object_produce(stars_game_situation, object_list)
close_count_all(object_list, set_list)
chain_of_stars(set_list)
replace_0(set_list, stars_game_situation)
lomove_all(stars_game_situation)
print_game_situation(stars_game_situation)