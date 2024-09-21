"""
                    关于高阶函数的练习
"""


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
# 练习一：([1, 1, 1], [2, 2], [3, 3, 3, 3])获取元组中长度最大的列表
list01 = ([1, 1, 1], [2, 2], [3, 3, 3, 3])
re01 = max(list01, key=lambda item01: len(item01))
print(re01)
# 练习二：获取敌人列表中所有名字，血量与攻击力
for item in map(lambda item01: (item01.name, item01.hp, item01.atk), Enemy.enemy_all_list):
    print(item)
# 练习三：获取敌人列表中攻击力大于100的活人
for item in filter(lambda item01: item01.atk > 100 and item01.hp > 0, Enemy.enemy_all_list):
    print(item)
# 练习四：根据防御力对敌人列表降序排列
re02 = sorted(Enemy.enemy_all_list, key=lambda item01: item01.defence, reverse=True)
for item in re02:
    print(item)
