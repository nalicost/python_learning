"""
                    计算圆锥体体积
"""
import random
# 随机获取两个十以内数字
radius, height = random.sample(range(1, 10), 2)
# 计算体积
v = 3.14 * radius ** 2 * height / 3
# 输出计算结果
print('圆锥的半径为：%d，高为：%d，体积为：%.2f' % (radius, height, v))
