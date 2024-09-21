"""
                    逆波兰表达式
"""


class DC:
    def __init__(self):
        self.stack_ = []

    def __push(self, item):
        if item in ('+', '-', '*', '/'):
            re = self.__calculate(item, self.__pop(), self.__pop())
            self.__push(str(re))
            print(self.__top())
        else:
            self.stack_.append(float(item))

    def __pop(self):
        return self.stack_.pop()

    def __top(self):
        return self.stack_[-1]

    @staticmethod
    def __multiply(x, y):
        return x * y

    @staticmethod
    def __minus(x, y):
        return x - y

    @staticmethod
    def __divide(x, y):
        return x / y

    @staticmethod
    def __add(x, y):
        return x + y

    def __calculate(self, str_symbol, x, y):
        symbol_dict = {'+': self.__add, '-': self.__minus, '*': self.__multiply, '/': self.__divide}
        return symbol_dict[str_symbol](y, x)

    def input_(self):
        str_calculate = input('请使用逆波兰表达式:>')
        if str_calculate:
            for item in str_calculate[3:len(str_calculate) - 2:2]:
                self.__push(item)
        return str_calculate


if __name__ == '__main__':
    a = DC()
    c = 1
    while c:
        c = a.input_()
