"""
                生成器表达式练习与对比
"""
# 练习一： 返回列表的bool值，返回列表的float值，以三种方式（生成器函数，生成器表达式，列表推导式）
list01 = [1, 2, 3.5, 4, 5.5, True, False, True, '10', '55', '3.4', 10.4]


def my_generator_01(target_list):
    for i in target_list:
        if isinstance(i, bool):
            yield i


for item in my_generator_01(list01):
    print(item)
# -------------------------------
my_generator_02 = (i for i in list01 if isinstance(i, bool))
for item in my_generator_02:
    print(item)
# -----------------------------------
my_list_01 = [i for i in list01 if isinstance(i, bool)]
for item in my_list_01:
    print(item)
# ----------------------------------
# ----------------------------------


def my_generator_03(target_list):
    for i in target_list:
        if isinstance(i, float):
            yield i


for item in my_generator_03(list01):
    print(item)
# ------------------------------
my_generator_04 = (i for i in list01 if isinstance(i, float))
for item in my_generator_03(list01):
    print(item)
# ------------------------------
my_list_02 = [i for i in list01 if isinstance(i, float)]
for item in my_list_02:
    print(item)
# 练习二：获取攻击比例大于6的技能，使用生成器函数和生成器表达式完成


class Skill:
    def __init__(self, id, name, atk_ratio, duration):
        self.id = id
        self.name = name
        self.atk_ratio = atk_ratio
        self.duration = duration

    def __str__(self):
        return f'{self.id},{self.name},{self.atk_ratio},{self.duration}'


list02 = [Skill(101, '乾坤大挪移', 5, 10),
          Skill(102, '降龙十八掌', 8, 5),
          Skill(103, '葵花宝典', 10, 2)
          ]


def my_generator_05(target_list):
    for i in target_list:
        if i.atk_ratio >= 6:
            yield i


for item in my_generator_05(list02):
    print(item)

my_generator_09 = (i for i in list02 if i.atk_ratio >= 6)
for item in my_generator_09:
    print(item)
# 练习三：获取持续时间在4-11之间的所有技能，使用生成器函数和生成器表达式完成


def my_generator_06(target_list):
    for i in target_list:
        if 4 <= i.duration <= 11:
            yield i


for item in my_generator_06(list02):
    print(item)

my_generator_10 = (i for i in list02 if 4 <= i.duration <= 11)
for item in my_generator_10:
    print(item)
# 练习四：获取编号是102的技能，使用生成器函数和生成器表达式完成


def my_generator_07(target_list):
    for i in target_list:
        if i.id == 102:
            return i


print(my_generator_07(list02))
# 练习五：获取技能名称大于四个字并且持续时间小于6的所有技能，使用生成器函数和生成器表达式完成


def my_generator_08(target_list):
    for i in target_list:
        if len(i.name) > 4 and i.duration < 6:
            yield i


for item in my_generator_08(list02):
    print(item)

my_generator_12 = (i for i in list02 if len(i.name) > 4 and i.duration < 6)
for item in my_generator_12:
    print(item)

from common.list_helper import *


def fun01(target):
    return target.name == '葵花宝典'


def fun02(target):
    return target.id == 101


def fun03(target):
    return target.duration > 0


print(ListHelper.get_element_single(list02, fun01))
print(ListHelper.get_element_single(list02, fun02))
print(ListHelper.get_element_single(list02, fun03))
print(ListHelper.get_element_single(list02, lambda target: target.name == '葵花宝典'))
print(ListHelper.get_element_single(list02, lambda target: target.id == 101))
print(ListHelper.get_element_single(list02, lambda target: target.duration > 0))
print(ListHelper.calculate_sum(list02, lambda i: i.duration <= 5))
print(ListHelper.calculate_sum(list02, lambda i: len(i.name) > 4))