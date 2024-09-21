"""
                    简单人名对话
"""
# 从命令台读取用户名称
name = input('请输入姓名>:')
# 名字对话
print('{}同学，学好Python，前途无量！'.format(name))
print('{}大侠，学好Python，大展拳脚！'.format(name[0]))
print('{}哥哥，学好Python，人见人爱！'.format(name[1:]))
