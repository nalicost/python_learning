"""
                    次方计算，获取最值
"""
# 获取两个数的值
num_1 = int(input('请输入a的值>:'))
num_2 = int(input('请输入b的值>:'))
# 输出结果
print(f'{num_1}的{num_2}次方是{num_1 ** num_2}')
print(f'{num_2}的{num_1}次方是{num_2 ** num_1}')
print(f'最大值是：{max(num_1 ** num_2, num_2 ** num_1)}')
