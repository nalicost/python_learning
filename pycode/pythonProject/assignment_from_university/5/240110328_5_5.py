# -*- encoding:gbk -*-
import random
success_num = 0
for i in range(5):
    if i - success_num > 1:
        print('��Ǹ������ʧ�ܣ�')
        break
    num_1, num_2 = random.sample(range(100), 2)
    print(f'�����{num_1}+{num_2}=')
    num_get = input('���������������>:')
    if int(num_get) == num_1 + num_2:
        success_num += 1
    else:
        print('�ش����')
else:
    print('��ϲ�����سɹ���')
