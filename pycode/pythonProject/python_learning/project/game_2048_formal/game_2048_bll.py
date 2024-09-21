"""
                    2048游戏核心算法——业务逻辑层
"""
from game_2048_model import *
import copy
import random


class GameCoreController:
    def __init__(self):
        self.__game_list = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.__count = 0
        self.__num_yield_range_list = []

    @staticmethod
    def __list_left_move(list_target):
        """
                单行左移
        :param list_target:对应行的列表
        """
        for i in range(len(list_target) - 1):
            for j in range(len(list_target) - 1):
                if list_target[j] == 0:
                    list_target[j], list_target[j + 1] = list_target[j + 1], list_target[j]
        GameCoreController.__list_sum_same(list_target)

    @staticmethod
    def __list_right_move(list_target):
        """
                单行右移
        :param list_target:对应行的列表
        """
        list_target.reverse()
        GameCoreController.__list_left_move(list_target)
        GameCoreController.__list_sum_same(list_target)
        list_target.reverse()

    def __list_up_move(self):
        """
                二维列表上移
        """
        self.__square_transform()
        self.__list_left_move_all()
        self.__square_transform()

    def __list_down_move(self):
        """
                二维列表下移
        """
        self.__square_transform()
        self.__list_right_move_all()
        self.__square_transform()

    def __square_transform(self):
        """
                二维列表矩阵转置
        """
        for i in range(1, len(self.__game_list)):
            for k in range(0, i):
                self.__game_list[i][k], self.__game_list[k][i] = self.__game_list[k][i], self.__game_list[i][k]

    @staticmethod
    def __list_sum_same(list_target):
        """
                单行列表相同数字相加
        :param list_target: 对应行的列表
        """
        zero_num = list_target.count(0) + 1
        while list_target.count(0) != zero_num:
            zero_num = list_target.count(0)
            for i in range(len(list_target) - 1):
                if list_target[i] == list_target[i + 1]:
                    list_target[i + 1] = list_target[i + 1] * 2
                    del list_target[i]
                    list_target.append(0)

    def __list_left_move_all(self):
        """
                二维列表全部左移
        """
        for i in self.__game_list:
            GameCoreController.__list_left_move(i)

    def __list_right_move_all(self):
        """
                二维列表全部左移
        """
        for i in self.__game_list:
            GameCoreController.__list_right_move(i)

    def is_continue(self):
        """
                判断游戏是否继续
        """
        list_backup = copy.deepcopy(self.__game_list)
        self.__list_up_move()
        self.__list_down_move()
        self.__list_right_move_all()
        self.__list_left_move_all()
        for i in self.__game_list:
            if 0 in i:
                self.__game_list = list_backup
                return True
        return False

    def random_num_produce(self):
        """
                二维列表随机数字生成
        """
        self.__num_random_range_produce()
        loc = LocationModel(*random.sample(self.__num_yield_range_list, 1)[0])
        add_list = [2] if self.__count < 254 else [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4] if self.__count < 512 else \
            [2, 2, 2, 2, 4]
        self.__game_list[loc.x][loc.y] = random.sample(add_list, 1)[0]

    def __num_random_range_produce(self):
        """
                二维列表可生成数字范围生成
        """
        self.__num_yield_range_list = []
        for key in range(len(self.__game_list)):
            for value in range(len(self.__game_list)):
                if self.__game_list[key][value] == 0:
                    self.__num_yield_range_list.append((key, value))
                self.__sum_num(key, value)

    def __sum_num(self, key, value):
        """
                二位列表中所有数字的加和
        :param key: 纵向索引
        :param value: 横向索引
        """
        self.__count += self.__game_list[key][value]

    @property
    def game_list(self):
        return self.__game_list

    def move(self, dir_0):
        """
            移动列表
        :param dir_0:为DirectionModel类型，移动方向
        """
        back_up_game_list = copy.deepcopy(self.__game_list)
        def_direction_tuple = (self.__list_up_move, self.__list_down_move,
                               self.__list_left_move_all, self.__list_right_move_all)
        def_direction_tuple[dir_0]()
        if self.__is_void_move(back_up_game_list):
            self.__game_list[::] = back_up_game_list
            return False
        return True

    def game_list_clear(self):
        self.__game_list = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    def __is_void_move(self, back_up_game_list):
        return back_up_game_list == self.__game_list


# --------------测试代码------------------------
if __name__ == '__main__':
    g01 = GameCoreController()
    g01._GameCoreController__game_list = [[0, 4, 16, 2], [0, 0, 16, 2], [0, 0, 0, 4], [2, 0, 0, 2]]
    print('origin', g01.game_list)
    g01.is_continue()
    print('judge', g01.game_list)
    g01.random_num_produce()
    print('yield', g01.game_list)
    g01.move(DirectionModel.Up)
    print('up', g01.game_list)
    g01.move(DirectionModel.DOWN)
    print('down', g01.game_list)
    g01.move(DirectionModel.LEFT)
    print('left', g01.game_list)
    g01.move(DirectionModel.RIGHT)
    print('right', g01.game_list)
    g01.random_num_produce()
    print('yield', g01.game_list)
