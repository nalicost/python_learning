"""
                以递归方式求阶乘
"""
# 通过将数据封装，较麻烦


def get_factorial_origin(num):
    """
            定义乘数与累成次数
        param num：int类型，需要求阶乘的数字
        return：int类型，阶乘运算的值
    """
    origin_value = 0
    len_ = num

    def get_factorial(num_):
        """
                阶乘累乘器
            param：int类型，上一次累乘的结果
            return：int类型，阶乘结果
        """
        nonlocal origin_value
        origin_value += 1
        if origin_value < len_:
            num_ = origin_value * num_
            return get_factorial(num_)
        else:
            return num_

    return get_factorial(num)   


print(get_factorial_origin(5))
print(get_factorial_origin(5))


# 较简单的写法，每次递归返回乘以一次即可，注意循环条件


def recursion(num):
    if num <= 1:
        return 1
    return num * recursion(num - 1)


print(recursion(5))
