# -*- encoding:gbk
str_input = input('�������ַ���>:')
str_list = []
for item in str_input:
    if item not in str_list:
        str_list.append(item)
str_result = ''.join(str_list)
print('ȥ�غ�Ľ��Ϊ��', str_result)
