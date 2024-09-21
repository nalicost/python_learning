"""
                        简单的对象与类的语法练习
"""


class Computer:
    def __init__(self, keyboard_price, mouse_price, fan_price):
        self.keyboard_price = keyboard_price
        self.mouse_price = mouse_price
        self.fan_price = fan_price

    def display_item(self):
        print(self.keyboard_price, self.mouse_price, self.fan_price)


computer_01 = Computer(100, 250, 450)
computer_02 = Computer(200, 350 ,600)
computer_01.display_item()
computer_02.display_item()


class Assignment:
    def __init__(self, subject, num):
        self.subject = subject
        self.num = num

    def display_item(self):
        print(self.subject, self.num)


assignment_01 = Assignment('数学', 3)
assignment_02 = Assignment('语文', 4)
assignment_01.display_item()
assignment_02.display_item()
