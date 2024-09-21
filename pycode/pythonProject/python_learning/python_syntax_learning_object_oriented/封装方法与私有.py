"""
        封装方法与私有化
"""
# 过渡版本1，以方法保护实例变量，通过方法封装私有变量


class Enemy:
    def __init__(self, name, hp, atk):
        self.set_name(name)
        self.set_hp(hp)
        self.set_atk(atk)

    def set_name(self, value):
        self.__name = value

    def set_hp(self, value):
        if 100 <= value <= 200:
            self.__hp = value
        else:
            raise ValueError('你有事吗')

    def set_atk(self, value):
        if 10 <= value <= 50:
            self.__atk = value
        else:
            raise ValueError('你有事吗')

    def get_name(self):
        return self.__name

    def get_hp(self):
        return self.__hp

    def get_atk(self):
        return self.__atk


enemy_01 = Enemy('黑手党', 200, 15)
# 过渡版本2，通过property保护实例变量，以类变量为中转，将输入的值依据行为放入对应函数的参数中执行


class Enemy:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk

    def __set_name(self, value):
        self.__name = value

    def __set_hp(self, value):
        if 100 <= value <= 200:
            self.__hp = value
        else:
            raise ValueError('你有事吗')

    def __set_atk(self, value):
        if 10 <= value <= 50:
            self.__atk = value
        else:
            raise ValueError('你有事吗')

    def __get_name(self):
        return self.__name

    def __get_hp(self):
        return self.__hp

    def __get_atk(self):
        return self.__atk

    name = property(__get_name, __set_name)
    hp = property(__get_hp, __set_hp)
    atk = property(__get_atk, __set_atk)


enemy_01 = Enemy('黑手党', 200, 15)
print(enemy_01.hp)
enemy_01.hp = 150
print(enemy_01.hp)
# 最终版本3，将上方使用与实例变量名字相同的类变量以@property与@.setter替换，增加可读性，若要设置只写，只能用过度版本2


class Enemy:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        if 100 <= value <= 200:
            self.__hp = value
        else:
            raise ValueError('你有事吗')

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        if 10 <= value <= 50:
            self.__atk = value
        else:
            raise ValueError('你有事吗')


enemy_01 = Enemy('黑手党', 200, 15)
print(enemy_01.hp)
enemy_01.hp = 150
print(enemy_01.hp)
