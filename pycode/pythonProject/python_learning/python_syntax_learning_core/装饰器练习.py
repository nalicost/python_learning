"""
                        装饰器练习
"""
import time


def identify_permission(func):
    def wrapper(*args, **kwargs):
        print('身份验证')
        func(*args, **kwargs)

    return wrapper


@identify_permission
def deposit(money):
    print(f'存{money}元')


@identify_permission
def withdraw(log_id, psw):
    print(f'取钱了，{log_id}，{psw}')


deposit(10000)
withdraw('abc', 123456)


def execute_time(func):
    def wrapper(*args, **kwargs):
        time_start = time.time()
        func(*args, **kwargs)
        time_end = time.time()
        print(f'执行时间：{time_end - time_start}')

    return wrapper


@execute_time
def fun01():
    time.sleep(2)
    print('fun01执行完毕')


@execute_time
def fun02(a):
    time.sleep(1)
    print('fun01执行完毕，参数是：', a)


fun01()
fun02(1)
