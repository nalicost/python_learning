# -*- encoding:gbk
parameter_input = input('��������������3����������Ӣ�Ķ��ţ�,���ָ�>:')
parameter_list = parameter_input.split(',')
for item in range(len(parameter_list)):
    print(f'��{item + 1}�������ǣ�', parameter_list[item])
print('ǰ���������ֱ���', '��'.join(parameter_list[0:3]))
