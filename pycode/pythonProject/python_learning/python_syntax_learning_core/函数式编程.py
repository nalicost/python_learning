"""
                函数式编程（面向函数开发）
"""
list_01 = [43, 4, 5, 5, 6, 7, 87]
# 需求一：在列表中查找所有偶数
# 需求二：在列表中查找所有大于10的数
# 需求三： 在列表中查找所有10--50之间的数
# 要求先用生成器，后使用函数式编程


def get_even_numbers(target_list):
    for item in target_list:
        if item % 2 == 0:
            yield item


def get_over_10(target_list):
    for item in target_list:
        if item > 10:
            yield item


def get_between_10_50(target_list):
    for item in target_list:
        if 10 <= item <= 50:
            yield item


list_generator = [get_even_numbers(list_01), get_over_10(list_01), get_between_10_50(list_01)]
for i in list_generator:
    for k in i:
        print(k)
    print('-------------分隔符--------------')


def get_num_required(target_list, func):
    for item in target_list:
        if func(item):
            yield item


def judge_even_num(item):
    return item % 2 == 0


def judge_over_10(item):
    return item > 10


def judge_between_10_50(item):
    return 10 <= item <= 50


list_def = [get_num_required(list_01, judge_even_num),
            get_num_required(list_01, judge_over_10),
            get_num_required(list_01, judge_between_10_50)
            ]
for i in list_def:
    for k in i:
        print(k)
    print('-------------分隔符--------------')
from common.list_helper import *


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

    def __str__(self):
        return f'{self.name},{self.hp},{self.atk},{self.defence}'


creat_01 = Enemy('灭霸', 5000, 300, 500)
creat_02 = Enemy('擎天柱', 0, 500, 200)
creat_03 = Enemy('铠甲勇士', 900, 100, 50)
creat_04 = Enemy('僵尸', 0, 300, 10)
creat_05 = Enemy('向日葵', 0, 300, 5)
print(ListHelper.get_element_single(Enemy.enemy_all_list, lambda item: item.name == '灭霸'))
for things in ListHelper.get_elements_all(Enemy.enemy_all_list, lambda item: item.atk > 10):
    print(things)
print(ListHelper.calculate_sum(Enemy.enemy_all_list, lambda item: item.hp > 0))
print(ListHelper.judge_element_exist(Enemy.enemy_all_list, lambda item: item.name == '成昆'))
print(ListHelper.judge_element_exist(Enemy.enemy_all_list, lambda item: item.atk < 5 or item.defence < 10))
print(ListHelper.sum_elements(Enemy.enemy_all_list, lambda item: item.hp))
print(ListHelper.sum_elements(Enemy.enemy_all_list, lambda item: item.atk))
print(ListHelper.sum_elements(Enemy.enemy_all_list, lambda item: item.defence))
print(list(ListHelper.select_elements(Enemy.enemy_all_list, lambda item: item.name)))
print(list(ListHelper.select_elements(Enemy.enemy_all_list, lambda item: item.atk)))
print(list(ListHelper.select_elements(Enemy.enemy_all_list, lambda item: (item.name, item.hp))))
print(ListHelper.index_max(Enemy.enemy_all_list, lambda item: item.atk))
print(ListHelper.index_max(Enemy.enemy_all_list, lambda item: item.hp))
print(ListHelper.index_max(Enemy.enemy_all_list, lambda item: item.defence))
ListHelper.queue_list(Enemy.enemy_all_list, lambda item: item.atk)
for i in Enemy.enemy_all_list:
    print(i)
ListHelper.queue_list(Enemy.enemy_all_list, lambda item: item.hp)
for i in Enemy.enemy_all_list:
    print(i)
ListHelper.queue_list(Enemy.enemy_all_list, lambda item: item.defence)
for i in Enemy.enemy_all_list:
    print(i)
print('--------------------------------')
ListHelper.delete_elements(Enemy.enemy_all_list, lambda item: item.atk < 50)
for i in Enemy.enemy_all_list:
    print(i)
print('--------------------------------')
ListHelper.delete_elements(Enemy.enemy_all_list, lambda item: item.defence > 100)
for i in Enemy.enemy_all_list:
    print(i)
print('--------------------------------')
ListHelper.delete_elements(Enemy.enemy_all_list, lambda item: item.hp == 0)
for i in Enemy.enemy_all_list:
    print(i)
print('--------------------------------')
