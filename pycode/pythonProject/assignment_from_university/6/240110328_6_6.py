# -*- encoding:gbk
parameter_input = input('请输入多个（大于3）参数，用英文逗号（,）分割>:')
parameter_list = parameter_input.split(',')
for item in range(len(parameter_list)):
    print(f'第{item + 1}个参数是：', parameter_list[item])
print('前三个参数分别是', '、'.join(parameter_list[0:3]))
