# -*- encoding:gbk -*-
import random
success_num = 0
for i in range(5):
    if i - success_num > 1:
        print('抱歉！闯关失败！')
        break
    num_1, num_2 = random.sample(range(100), 2)
    print(f'请计算{num_1}+{num_2}=')
    num_get = input('请输入你的运算结果>:')
    if int(num_get) == num_1 + num_2:
        success_num += 1
    else:
        print('回答错误')
else:
    print('恭喜：闯关成功！')
