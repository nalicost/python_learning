"""
            不同请求类型的逻辑处理
"""
import time


def get_time():
    return f'<h1>{time.ctime()}</h1>'


def bye():
    return '<h1>bye</h1>'


def hello():
    return '<h1>hello</h1>'
