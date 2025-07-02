# -*- encoding:gbk
str_input = input('请输入字符串>:')
str_list = []
for item in str_input:
    if item not in str_list:
        str_list.append(item)
str_result = ''.join(str_list)
print('去重后的结果为：', str_result)
