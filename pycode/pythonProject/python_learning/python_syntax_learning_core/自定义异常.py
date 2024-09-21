"""
            自定义异常
"""


class AttackRangError(Exception):
    def __init__(self, message, error_code_line, error_code, atk):
        super().__init__(message)
        self.error_code = error_code
        self.error_code_line = error_code_line
        self.atk = atk


class Enemy:
    def __init__(self, atk):
        self.atk = atk

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        if 1 <= value <= 100:
            self.__atk = value
        else:
            raise AttackRangError('攻击力超出范围', 24, 'if 1 <= value <= 100:', value)


try:
    enemy = Enemy(1000)
except AttackRangError as error_01:
    print(error_01.error_code, error_01.error_code_line)
