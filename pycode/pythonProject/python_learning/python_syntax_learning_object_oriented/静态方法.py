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


double_list = [
    ['00', '01', '02', '03'],
    ['10', '11', '12', '13'],
    ['20', '21', '22', '23'],
]
dir_01 = DirectionOfElements.get_new_position('13', double_list)
print(dir_01.vector2_x, dir_01.vector2_y)
dir_01_after_process_1 = DirectionOfElements.move(dir_01, DirectionOfElements.lerg_move_vector, -1, 3, double_list)
dir_01 = DirectionOfElements.get_new_position('22', double_list)
print(dir_01.vector2_x, dir_01.vector2_y)
dir_01_after_process_2 = DirectionOfElements.move(dir_01, DirectionOfElements.uplo_move_vector, -1, 2, double_list)
dir_01 = DirectionOfElements.get_new_position('03', double_list)
print(dir_01.vector2_x, dir_01.vector2_y)
dir_01_after_process_3 = DirectionOfElements.move(dir_01, DirectionOfElements.uplo_move_vector, 1, 2, double_list)
print(dir_01_after_process_1, dir_01_after_process_2, dir_01_after_process_3)


# 练习二：敌人类


class Enemy:
    enemy_all_list = []

    def __init__(self, name, hp, atk, defence):
        """
                敌人的数据成员
        :param name: 名字
        :param hp: 生命值
        :param atk: 攻击力
        :param defence: 防御力
        """
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defence = defence
        Enemy.enemy_all_list.append(self)

    def print_enemy_info(self):
        """
                打印敌人信息
        """
        print(f'name:{self.name},hp:{self.hp},atk:{self.atk},defence:{self.defence}')

    @classmethod
    def index_enemy(cls, index_section, index_content):
        """
                寻找对应敌人信息
        :param index_section: 寻找敌人信息的所属类型
        :param index_content: 寻找敌人信息的内容
        """
        for item in cls.enemy_all_list:
            item_dict = {'name': item.name, 'hp': item.hp, 'atk': item.atk, 'defence': item.defence}
            # 调出所有对象的实例变量，供后方判断
            if item_dict[index_section] == index_content:
                item.print_enemy_info()

    @classmethod
    def calculate_enemy_average_atk(cls):
        """
                计算平均攻击力
        :return: 平均攻击力的值
        """
        k = 0
        for item in cls.enemy_all_list:
            k += item.atk
        return k / len(cls.enemy_all_list)

    @classmethod
    def del_object_lower_10(cls):
        """
                删除防御力低于10的敌人
        """
        for item in range(len(cls.enemy_all_list) - 1, -1, -1):
            if Enemy.is_defence_lower_10(cls.enemy_all_list[item]):
                Enemy.enemy_all_list.remove(cls.enemy_all_list[item])

    @classmethod
    def add_data_atk(cls, num):
        """
                增加所有敌人的攻击力
        :param num: 增加数量
        """
        for item in cls.enemy_all_list:
            item.atk += num

    @classmethod
    def print_all_enemy_info(cls):
        """
                打印所有敌人信息
        """
        for item in cls.enemy_all_list:
            item.print_enemy_info()

    @staticmethod
    def is_defence_lower_10(item):
        """
                判断敌人防御力是否低于10
        :param item: 判断对象
        :return: bool值
        """
        return item.defence < 10


creat_01 = Enemy('灭霸', 5000, 300, 500)
creat_02 = Enemy('擎天柱', 0, 500, 200)
creat_03 = Enemy('铠甲勇士', 900, 100, 50)
creat_04 = Enemy('僵尸', 0, 300, 10)
creat_05 = Enemy('向日葵', 0, 300, 5)
Enemy.index_enemy('name', '灭霸')
Enemy.index_enemy('hp', 0)
print(Enemy.calculate_enemy_average_atk())
Enemy.add_data_atk(50)
Enemy.print_all_enemy_info()
Enemy.del_object_lower_10()
print('-------------------------')
Enemy.print_all_enemy_info()
