"""
        面向对象思想练习
"""
# 练习1，要求：张无忌教赵敏九阳神功    赵敏教张无忌化妆   张无忌上班挣了10000    赵敏上班挣了6000


class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def teach(self, student, skill):
        print(self.__name, '教', student.name, skill.name)

    def work(self, result):
        print(self.__name, '工作挣了', result.num)


class Skill:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


class Money:
    def __init__(self, num):
        self.num = num

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, value):
        self.__num = value


person_01 = Person('张无忌')
person_02 = Person('赵敏')
skill_01 = Skill('九阳神功')
skill_02 = Skill('化妆')
money_01 = Money(10000)
money_02 = Money(6000)
person_01.teach(person_02, skill_01)
person_02.teach(person_01, skill_02)
person_01.work(money_01)
person_02.work(money_02)
# 练习二，以面向对象的思想描述一下场景，玩家攻击敌人，敌人受伤掉血，可能死亡，爆装备和分数；敌人攻击玩家，玩家受伤掉血碎屏，可能死亡，游戏结束


class Player:
    def __init__(self, name, hp, atk, score, equipment):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.score = score
        self.equipment = equipment

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
        self.__hp = value

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        self.__atk = value

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value

    @property
    def equipment(self):
        return self.__equipment

    @equipment.setter
    def equipment(self, value):
        self.__equipment = value

    def __print_info(self):
        print(self.__name, self.__hp, self.__score, self.__equipment)

    def self_hurt(self, value):
        self.hp -= value.atk
        self.__player_situation()

    def attack_enemy(self, enemy):
        enemy.self_hurt(self)

    def __player_situation(self):
        if self.hp <= 0:
            print('wasted，游戏结束')
        else:
            print('碎屏', '小心了')
            self.__print_info()

    def player_reward(self, enemy):
        self.score += enemy.score
        for item in enemy.equipment:
            self.equipment.append(item)
        print('你真棒，敌人死了')
        self.__print_info()


class Enemy:
    def __init__(self, name, hp, atk, score, equipment):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.score = score
        self.equipment = equipment

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
        self.__hp = value

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        self.__atk = value

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value

    @property
    def equipment(self):
        return self.__equipment

    @equipment.setter
    def equipment(self, value):
        self.__equipment = value

    def __print_info(self):
        print(self.__name, self.__hp, self.__score, self.__equipment)

    def self_hurt(self, value):
        self.hp -= value.atk
        self.__enemy_situation(value)

    def attack_player(self, player):
        player.self_hurt(self)

    def __enemy_situation(self, value):
        if self.hp <= 0:
            print('掉装备')
            value.player_reward(self)
        else:
            self.__print_info()


player_01 = Player('aa', 200, 50, 0, ['无锋剑'])
enemy_01 = Enemy('超级破坏王', 50, 400, 50, ['合金钻头'])
enemy_02 = Enemy('joker', 500, 40, 50, ['纸牌'])
player_01.attack_enemy(enemy_01)
player_01.attack_enemy(enemy_02)
enemy_02.attack_player(player_01)
enemy_01.attack_player(player_01)
