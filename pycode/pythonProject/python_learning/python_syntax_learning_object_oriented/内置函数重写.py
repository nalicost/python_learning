"""
            内置函数是可重写的，本次练习，仅展示两种，剩余自行百度
"""
# 练习一：定义enemy类，并生成对象，打印对象（自定义格式），并克隆一个对象


class Enemy:
    def __init__(self, name, atk, defence, hp):
        self.name = name
        self.atk = atk
        self.defence = defence
        self.hp = hp

    def __str__(self):
        return f'name:{self.name},atk:{self.atk},defence:{self.defence},hp:{self.hp}'

    def __repr__(self):
        return f"Enemy('{self.name}', {self.atk}, {self.defence}, {self.hp})"
        # 如果不希望变量引号被去掉，多加一层引号


e01 = Enemy('Hancer', 100, 50, 50)
print(e01)
e02 = eval(repr(e01))
e01.name = 'haha'
print(e02.name)
