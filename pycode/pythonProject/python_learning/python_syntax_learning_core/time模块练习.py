"""
                    对time模块的部分功能练习
"""
import time
# 练习一：根据年月日获取星期几
time_tuple_0 = time.localtime(time.time())
year, month, day = time_tuple_0[0:3]


def get_week(year_now, month_now, day_now):
    """
                获取星期几
    :param year_now: 现在的年份
    :param month_now: 现在的月份
    :param day_now: 现在的天数
    :return: 中文的星期
    """
    week_day_tuple = ('星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日')
    time_tuple_1 = time.strptime(f'{year_now}{month_now}{day_now}', '%Y%m%d')
    the_day_in_a_week = time_tuple_1[6]
    return week_day_tuple[the_day_in_a_week]


print(get_week(year, month, day))

# 练习二：根据出生年月日，获取活的天数


def get_days_num_from_birth(year_birth, month_birth, day_birth):
    time_birth_seconds_all = time.mktime(time.strptime(f'{year_birth}{month_birth}{day_birth}', '%Y%m%d'))
    time_days_num_from_birth_seconds = time.time() - time_birth_seconds_all
    return time_days_num_from_birth_seconds // (3600 * 24)


print(get_days_num_from_birth(2005, 10, 25))