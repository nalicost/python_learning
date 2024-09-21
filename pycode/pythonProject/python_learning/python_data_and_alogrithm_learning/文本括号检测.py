"""
                    输入文本，检测括号是否配对
"""
from parso.parser import Stack
# 思路一：通过列表配对，即括号全部放入其中，成对删除


def parenthesis_transition_output01(tuple_):
    """
                括号符号转换
    :param tuple_: tuple类型，元组中包含两个元素（第一个为为数字的括号字符，第二个为在字符串中的索引）
    :return: tuple类型，数字符号转化为括号字符的元组
    """
    transition_dict = {0: '(', 15: ')', 1: '[', 16: ']', 2: '{', 17: '}', 3: '（', 18: '）', 4: '【', 19: '】'}
    # 取值时，保证同向括号的值域与异向括号的值域没有交集（保证下方判断未匹配括号，不会将未消去的同向括号算入其中），其次右括号的值大于左括号的值，
    # 使得剔除当两个匹配的括号相连接且其中嵌套括号不匹配倒置未消去，而错误的算入其中
    return transition_dict[tuple_[0]], tuple_[1]


def parenthesis_transition_input01(parenthesis_str):
    """
                括号符号转换
    :param parenthesis_str: str类型,括号字符
    :return: int类型，括号符号转化为整型
    """
    transition_dict = {'(': 0, ')': 15, '[': 1, ']': 16, '{': 2, '}': 17, '（': 3, '）': 18, '【': 4, '】': 19}
    return transition_dict[parenthesis_str]


def parenthesis_finder01(string_):
    """
                括号字符筛选
    :param string_: str类型，需要处理的字符串
    :return: list类型，列表中含字符串中所有转化后的括号字符
    """
    re_list = []
    # 将符号匹配转化为数字之差为1
    for item in range(len(string_)):
        if string_[item] in ('(', ')', '[', ']', '{', '}', '（', '）', '【', '】'):
            re_list.append((parenthesis_transition_input01(string_[item]), item))
    return re_list


def parenthesis_back_wrong01(list_):
    """
                返回未匹配的括号字符
    :param list_: list类型，经过数字符号转化的括号字符列表
    :return: bool/bool+tuple,即匹配或不匹配以及错误的内容
    """
    while list_:
        # 列表为空，说明配对
        temp = list_[::]
        parenthesis_matcher(list_)
        if temp == list_ and list_:
            # 删除内容，且列表不为空，则说明不匹配
            break
    else:
        return True
    for item in range(len(list_) - 1):
        if list_[item + 1][0] - list_[item][0] <= -11:
            # 只检测左右括号不匹配的情况
            return False, parenthesis_transition_output01(list_[item])
    else:
        # 如果不满足上面条件，说明括号错误为数量不匹配
        return False, parenthesis_transition_output01(list_[0])


def parenthesis_matcher(list_):
    """
                括号字符匹配删除器
    :param list_: list类型，经过数字符号转化的括号字符列表
    """
    for item in range(len(list_) - 1, 0, -1):
        try:
            if list_[item][0] - list_[item - 1][0] == 15:
                # 差一就都删除
                del list_[item - 1]
                del list_[item - 1]
                # 注意，由于删除前一个时，列表集体前移一个，后一个变为前一个，故应该再次删除前一个
        except IndexError:
            # 删除两个东西后，使得超出索引，处理异常
            continue


if __name__ == '__main__':
    str_ = input(':>')
    print(parenthesis_back_wrong01(parenthesis_finder01(str_)))


# 思路二：通过栈完成，类似逆波兰表达式，遇到左括号就放入栈，遇到右括号就取出栈中内容进行配对
from python_data_and_alogrithm_learning.stack import *


def parenthesis_transition02(tuple_):
    """
                括号符号转换
    :param tuple_: tuple类型，元组中包含两个元素（第一个为为数字的括号字符，第二个为在字符串中的索引）
    :return: tuple类型，数字符号转化为括号字符的元组
    """
    transition_dict = {0: '(', 1: ')', 3: '[', 4: ']', 6: '{', 7: '}', 9: '（', 10: '）', 12: '【', 13: '】'}
    return transition_dict[tuple_[0]], tuple_[1]


def parenthesis_transition_input02(parenthesis_str):
    """
                括号符号转换
    :param parenthesis_str: str类型,括号字符
    :return: int类型，括号符号转化为整型
    """
    transition_dict = {'(': 0, ')': 1, '[': 3, ']': 4, '{': 6, '}': 7, '（': 9, '）': 10, '【': 12, '】': 13}
    return transition_dict[parenthesis_str]


def parenthesis_finder02(string_):
    """
                括号字符筛选
    :param string_: str类型，需要处理的字符串
    :return: list类型，列表中含字符串中所有转化后的括号字符
    """
    re_list = []
    # 将符号匹配转化为数字之差为1
    for item in range(len(string_)):
        if string_[item] in ('(', ')', '[', ']', '{', '}', '（', '）', '【', '】'):
            re_list.append((parenthesis_transition_input02(string_[item]), item))
    return re_list


"""参考括号字符返回方法
def parenthesis_finder02(string_):
    # 使用生成器，减少内存压力
    for item in range(len(string_)):
        if string_[item] in ('(', ')', '[', ']', '{', '}', '（', '）', '【', '】'):
            yield string_[item], item
            
# 后面在matcher中，通过迭代生成器中的元素，并放入栈中，实现
# 除数字外的匹配方式：{'(': ')', '[': ']', '{': '}', '（': '）', '【': '】}
"""


def parenthesis_matcher01(list_):
    """
                括号字符匹配检测器
    :param list_: list类型，经过数字符号转化的括号字符列表
    :return: bool/bool+tuple,即匹配或不匹配以及错误的内容
    """
    stack = SStack()
    for item in list_:
        if item[0] in (0, 3, 6, 9, 12):
            stack.push(item)
        elif not stack.is_empty():
            if item[0] - stack.top()[0] == 1:
                stack.pop()
            else:
                return False, parenthesis_transition02(stack.pop())
        else:
            return False, parenthesis_transition02(item)
    return True


# if __name__ == '__main__':
#     str_ = input(':>')
#     print(parenthesis_matcher01(parenthesis_finder02(str_)))
