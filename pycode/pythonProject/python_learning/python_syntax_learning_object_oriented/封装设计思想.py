"""
        以面向对象的思想，完成小明去招商银行取钱
"""


class Person:
    person_money = 0

    def __init__(self, name, money):
        self.name = name
        self.money = money

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        self.__money = value

    def get_money(self, position):
        position.give_money(self.__money)
        if Bank.bank_money >= self.__money:
            Person.person_money += self.__money
            print(self.__name, '去', position.name, '取钱')
            print(Person.person_money)
        else:
            print('回家喝西北风')


class Bank:
    bank_money = 10000000

    def __init__(self, name):
        self.name = name

    def give_money(self, money):
        if Bank.bank_money >= money:
            Bank.bank_money -= money
            print(Bank.bank_money)
        else:
            print('银行付不起')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value



p_01 = Person('小明', 500000000000)
b_01 = Bank('招商银行')
p_01.get_money(b_01)