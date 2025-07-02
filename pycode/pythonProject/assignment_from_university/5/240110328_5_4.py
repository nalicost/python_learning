# -*- encoding:gbk -*-
num_judge = int(input('请输入一个整数>:'))
for i in range(2, num_judge):
    if num_judge % i == 0:
        print(f'{num_judge}不是质数')
        break
else:
    print(f'{num_judge}是质数')
