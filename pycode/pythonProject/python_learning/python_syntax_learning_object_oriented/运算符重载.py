"""
                    对运算符的重载，实际就是再定义
"""
# 练习一：自定义类的减法，乘法


class Vector1:
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return f'({self.x})'

    def __sub__(self, other):
        return Vector1(self.x - other)

    def __mul__(self, other):
        return Vector1(self.x * other)

    def __rsub__(self, other):
        return Vector1(other - self.x)

    def __rmul__(self, other):
        return Vector1(self.x * other)

    def __isub__(self, other):
        self.x -= other
        return self


vector01 = Vector1(1)
print(vector01 * 2)
print(vector01 - 3)
print(2 * vector01)
print(3 - vector01)
vector01 -= 2
print(vector01)
