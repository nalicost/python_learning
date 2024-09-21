"""
                    列表助手
"""


class ListHelper:
    @staticmethod
    def get_elements_all(target_list, func):
        """
                    获取所有符合要求的列表中元素
        :param target_list: 目标列表
        :param func: 函数，有一个参数作为判断元素，返回值为bool，筛选要求
        :return: 符合要求元素的生成器
        """
        for i in target_list:
            if func(i):
                yield i

    @staticmethod
    def get_element_single(target_list, func):
        """
                    获取第一个符合要求的列表中元素
        :param target_list: 目标列表
        :param func: 函数,有一个参数作为判断元素，返回值为bool，筛选要求
        :return: 符合要求的第一个元素
        """
        for i in target_list:
            if func(i):
                return i

    @staticmethod
    def calculate_sum(target_list, func):
        """
                    计算符合要求元素的数量
        :param target_list: 目标列表
        :param func: 函数，有一个参数作为判断元素，返回值为bool，元素需符合的要求
        :return: 符合要求的元素数量
        """
        num = 0
        for i in target_list:
            if func(i):
                num += 1
        return num

    @staticmethod
    def judge_element_exist(target_list, func):
        """
                    判断符合要求的元素是否存在与列表中
        :param target_list: 目标列表
        :param func: 函数，返回bool，判断要求
        :return: bool
        """
        for item in target_list:
            if func(item):
                return True
        return False

    @staticmethod
    def sum_elements(target_list, func):
        """
                    累加所需的元素
        :param target_list: 目标列表
        :param func: 函数，传入处理的对象作为一个参数，返回需要累加的对象，对象中元素筛选逻辑
        :return: 累加值
        """
        re_value = 0
        for item in target_list:
            re_value += func(item)
        return re_value

    @staticmethod
    def select_elements(target_list, func):
        """
                    筛选对应的元素
        :param target_list: 目标列表
        :param func: 函数，对象作为一个参数，返回筛选要求对象的元素，对象中元素筛选要求逻辑
        :return: 生成器，筛选得到的对象
        """
        for item in target_list:
            yield func(item)

    @staticmethod
    def index_max(target_list, func):
        """
                    查找对应最大元素的对象
        :param target_list: 目标列表
        :param func: 函数，将需要比较的对象作为一个参数传入，返回需要比较对象中的元素，对象中元素筛选逻辑
        :return: 对应最大元素的对象
        """
        max_value = target_list[0]
        for item in range(1, len(target_list)):
            if func(max_value) < func(target_list[item]):
                max_value = target_list[item]
        return max_value

    @staticmethod
    def queue_list(target_list, func):
        """
                    依据指定对象中的元素升序排列列表中元素
        :param target_list: 目标列表
        :param func: 函数，需要排列对象作为一个参数，返回筛选对象的元素，元素筛选逻辑
        """
        for item01 in range(0, len(target_list) - 1):
            for item02 in range(0, len(target_list) - item01):
                if func(target_list[item01]) > func(target_list[item02]):
                    target_list[item01], target_list[item02] = target_list[item02], target_list[item01]

    @staticmethod
    def index_min(target_list, func):
        """
                    查找对应最小元素的对象
        :param target_list: 目标列表
        :param func: 函数，将需要比较的对象作为一个参数传入，返回需要比较对象中的元素，对象中元素筛选逻辑
        :return: 对应最小元素的对象
        """
        min_value = target_list[0]
        for item in range(1, len(target_list)):
            if func(min_value) > func(target_list[item]):
                min_value = target_list[item]
        return min_value

    @staticmethod
    def queue_list_reverse(target_list, func):
        """
                    依据指定对象中的元素降序排列列表中元素
        :param target_list: 目标列表
        :param func: 函数，需要排列对象作为一个参数，返回筛选对象的元素，元素筛选逻辑
        """
        for item01 in range(0, len(target_list) - 1):
            for item02 in range(0, len(target_list) - item01):
                if func(target_list[item01]) < func(target_list[item02]):
                    target_list[item01], target_list[item02] = target_list[item02], target_list[item01]

    @staticmethod
    def delete_elements(target_list, func):
        """
                    依据指定要求删除列表中的元素
        :param target_list: 目标列表
        :param func: 函数，需要列表的对象作为一个参数，返回bool，元素筛选逻辑
        """
        for item in range(len(target_list) - 1, -1, -1):
            if func(target_list[item]):
                del target_list[item]
