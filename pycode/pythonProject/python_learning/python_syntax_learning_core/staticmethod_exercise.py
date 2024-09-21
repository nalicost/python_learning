"""
        对静态方法的两个练习
"""


# 练习一：二维列表的移动与位置获取


class DirectionOfElements:
    def __init__(self, direction_elements):
        """
                二位列表中位置的数据成员
        :param direction_elements: 横纵坐标
        :param vector_x: 向量横坐标
        :param vector_y: 向量纵坐标
        """
        self.vector2_x = int(direction_elements[0])
        self.vector2_y = int(direction_elements[1])

    @staticmethod
    def lerg_move_vector(direction):
        """
                水平基向量
        :param direction: 水平基向量的长度
        :return: 水平基向量
        """
        return 0, direction

    @staticmethod
    def uplo_move_vector(direction):
        """
                竖直基向量
        :param direction: 竖直基向量的长度
        :return: 竖直基向量
        """
        return direction, 0

    def move(self, method, direction, count, target_list):
        """
                坐标移动
        :param method: 竖直水平方向移动的方法选择
        :param direction: 起始位置
        :param count: 移动距离
        :param target_list: 移动所在的二维列表
        :return: 移动过程
        """
        direction_move_process = []
        unit_vector = method(direction)
        # 向量加减完成移动
        for i in range(count):
            self.vector2_x = self.vector2_x + unit_vector[0]
            self.vector2_y = self.vector2_y + unit_vector[1]
            direction_move_process.append(target_list[self.vector2_x][self.vector2_y])
        return direction_move_process

    @staticmethod
    def get_new_position(index_target, target_list):
        """
                获取新的位置
        :param index_target: 需要寻找位置的对象
        :param target_list: 目标所在的二维列表
        :return:
        """
        return DirectionOfElements((index_target[0], index_target[1]))





