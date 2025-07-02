"""
                日期和时间的输出
"""
from datetime import datetime
# 获取当前日期和时间信息
now = datetime.now()
# 输出时间
print(now)
# 输出日期部分
print(now.strftime('%x'))
# 输出时间部分
print(now.strftime('%X'))
