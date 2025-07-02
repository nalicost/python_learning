"""
                获取5位数的个位数和千位数
"""


def repeater_get_input(func, request_sentence, repeat_time=0):
    """
    :param func: 函数，处理从命令台获取的内容
    :param request_sentence: str类型，提示输入
    :param repeat_time: int类型，重复次数
    """
    # 计数重复执行的次数
    i = 0
    # 满足重复次数退出
    while i <= repeat_time - 1:
        # 防止非法输入
        try:
            # 从命令台获取用户输入需要处理的数字，并传入处理函数
            print(func(input(f'{request_sentence}>:')))
        except Exception:
            # 出现错误给出提示
            print('请输入符合要求的数字')
            # 跳过错误的，防止占用循环次数
            continue
        # 计数器加一
        i += 1


def get_thousand_and_hundred(number):
    """
    :param number: str类型，要处理的数字
    :return: tuple类型，获取的数字个位与千位
    """
    # 防止输入位数小于5
    if len(number) != 5:
        raise ValueError
    # 返回结果
    return f'个位：{int(number) % 10}，千位：{int(number) // 1000 % 10}'


if __name__ == '__main__':
    # 传入处理函数逻辑，传入提示语，传入重复次数
    repeater_get_input(get_thousand_and_hundred, request_sentence='请输入五位数字', repeat_time=4)
