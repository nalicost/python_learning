# -*- encoding:gbk -*-
num_judge = int(input('������һ������>:'))
for i in range(2, num_judge):
    if num_judge % i == 0:
        print(f'{num_judge}��������')
        break
else:
    print(f'{num_judge}������')
