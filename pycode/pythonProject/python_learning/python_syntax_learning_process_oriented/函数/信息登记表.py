"""
                                   用来注册、登记、查询，修改信息
                                                                                                                     """
import os

f_0 = open('信息表.txt', 'r', encoding='utf-8')
f_1 = open('信息表_backup.txt', 'w+', encoding='utf-8')
f_1.write(f_0.readline())  # 备份文件
id_all = {}
id_content = ['username', 'password', 'age', 'job', 'phone_number']
for line in f_0:
    f_1.write(line)  # 备份文件
    line = line.split(' ')  # 拆分文件，处理成需要的dict
    id_all[line[0]] = {}
    for k in range(len(id_content)):
        id_all[line[0]][id_content[k]] = line[k]  # 生成dict
f_0.close()
layer, username, password = 0, 1, 2  # 层数，用户名，密码，用来作为函数中的参数，并接收返回值


def out(layer, a='', b=''):
    """
                           程序退出函数
    :param layer: 当前的层数
    :param a: a为第一个input的值，默认为空字符串
    :param b: b为第二个input的值，默认为空字符串
    :return: 返回层数，用户名和密码
    """
    if a == 'b' or b == 'b':  # 下面两个为取消和退出模块下有类似，都是同一作用
        print('已取消')
        return layer, username, password
    elif a == 'q' or b == 'q':
        return -1, username, password


def rigister(username, password, choice, id_all, layer):  # 登录函数模块
    """
                           登录程序的函数
    :param username: 用户名
    :param password: 密码
    :param choice: 选择的功能
    :param id_all: 员工信息的字典
    :param layer: 当前所在层数
    :return: 返回层数，用户名和密码
    """
    while True:
        username = input('你的用户名是:>').strip()
        password = input('你的密码是:>').strip()
        if username == 'b' or password == 'b' or username == 'q' or password == 'q':
            return out(layer, username, password)
        elif username not in id_all and username != '':  # 检验用户名不存在
            for n in id_all.values():
                if n['password'] == password or password == '':  # 检验密码不存在
                    print('密码已存在或密码不合法')
                    break
            else:  # 增加用户名与密码
                id_all.setdefault(f'{username}',
                                  {'username': username, 'password': password, 'age': input('你的年龄是:>'),
                                   'job': input('你的工作是:>'), 'phone_number': input('你的电话号码是:>')})
                print('注册成功')
                return 0, username, password
        else:
            print('用户名已存在或用户名不合法')


def password_revise(username, password, choice, id_all, layer):  # 密码修改模块
    """
                           密码修改的函数
    :param username: 用户名
    :param password: 密码
    :param choice: 选择的功能
    :param id_all: 员工信息的字典
    :param layer: 当前所在层数
    :return: 返回层数，用户名和密码
    """
    while True:
        print('您当前的旧密码是：', password)
        password_new = (input('你的新密码是:>')).strip()
        password_confirm = (input('请确认密码:>')).strip()  # 密码确认
        if password_new == 'b' or password_confirm == 'b' or password_new == 'q' or password_confirm == 'q':
            return out(layer, password_new, password_confirm)
        elif password_new == password_confirm:
            if password_new not in id_all[username]['password'] and password_new != '':  # 确认密码不重复
                id_all[username]['password'] = password_new
                print('修改成功')
                password = password_new
                return 1, username, password
            else:
                print('密码重复或不合法')
        else:
            print('两次密码不一致')


def id_revise(username, password, choice, id_all, layer):  # 个人信息修改模块
    """
                               个人信息修改的函数
        :param username: 用户名
        :param password: 密码
        :param choice: 选择的功能
        :param id_all: 员工信息的字典
        :param layer: 当前所在层数
        :return: 返回层数，用户名和密码
        """
    list_content = ['username', 'age', 'job', 'phone_number']  # 用来对应修改项
    print(f'您当前的旧{list_content[choice]}是：', id_all[username][list_content[choice]])
    while True:
        id_new = (input(f'你的新{list_content[choice]}是:>')).strip()
        if id_new == 'b' or id_new == 'q':
            return out(layer, id_new)
        elif id_new == '':
            print('输入的修改内容不合法')
            continue
        elif choice != 0:  # 非用户名的修改
            if choice != 0:
                if choice == 1 and not id_new.isnumeric() or choice == 2 and id_new.isnumeric() or choice == 3 and not id_new.isnumeric():
                    print('修改内容不合法')
                    continue
            id_all[username][list_content[choice]] = id_new
        else:  # 用户名的修改
            id_all[id_new] = id_all[username]
            id_all[id_new]['username'] = id_new
            del id_all[username]
            username = id_new
        print('修改成功')
        return 1, username, password


def id_print(username, password, choice, id_all, layer):
    """
                               打印个人信息的函数
        :param username: 用户名
        :param password: 密码
        :param choice: 选择的功能
        :param id_all: 员工信息的字典
        :param layer: 当前所在层数
        :return: 返回层数，用户名和密码
        """
    print(f'{username}的个人信息'.center(50, '-'))
    for i, t in id_all[username].items():  # 打印dict中对应的个人信息
        print(i, ':', t)
    print('-' * 50)
    return 1, username, password


def enter(username, password, choice, id_all, layer):
    """
                               登录的函数
        :param username: 用户名
        :param password: 密码
        :param choice: 选择的功能
        :param id_all: 员工信息的字典
        :param layer: 当前所在层数
        :return: 返回层数，用户名和密码
        """
    i = 3
    while i != 0:
        username = input('你的用户名是:>').strip()
        password = input('你的密码是:>').strip()
        if username == 'b' or password == 'b' or username == 'q' or password == 'q':
            return out(layer, username, password)
        elif username in id_all:
            if password == id_all[username]['password']:  # 密码，用户名确认
                return 1, username, password
        i -= 1
        print(f'用户名错误，还剩{i}次机会')
    return -1, username, password


def progress(username, password, choice, id_all, layer):  # 进入下一层
    """
                               进入下一层的函数
        :param username: 用户名
        :param password: 密码
        :param choice: 选择的功能
        :param id_all: 员工信息的字典
        :param layer: 当前所在层数
        :return: 返回层数，用户名和密码
        """
    return 2, username, password


function_layer = {0: {0: {'注册新用户': rigister}, 1: {'登录账户': enter}},
                  1: {0: {'查询你的个人信息': id_print}, 1: {'修改你的个人信息': progress},
                      2: {'修改你的密码': password_revise}},
                  2: {0: {'修改你的用户名': id_revise}, 1: {'修改你的年龄': id_revise}, 2: {'修改你的工作': id_revise},
                      3: {'修改你的手机号码': id_revise}}} # 核心代码，通过字典对应各个功能层，并对接各个函数模块
while layer != -1:  # 应用结束条件
    if layer == 0:
        print('-' * 50)
    for m, v in function_layer[layer].items():  # 打印目录内容
        for n in v.keys():
            print(m, ':', n)
    choice = input('你选择的功能是:>').strip()  # 功能选择
    if choice == 'b':  # 退至上一层
        layer -= 1
        if layer == 0:  # 当从第一层至第零层时为退出登录
            print('已退出登录')
        elif layer > 0:
            print('已退至上一层')
        else:
            layer += 1  # 防止减到负一层，导致程序退出
            print('已在首页，无法退至上一层')
    elif choice == 'q':
        layer = -1
        print('期待下次使用')
    elif choice.isalpha() or choice == '':  # 不输内容或乱输内容的提示
        print('请输入指示中的内容')
    else:
        choice = int(choice)
        for s in function_layer[layer][choice].keys():
            layer, username, password = function_layer[layer][choice].get(s)(username, password, choice, id_all,
                                                                             layer)  # 函数使用并接受
    if layer == 1:
        print(f'欢迎用户{username}'.center(50, '-'))
    else:
        print('-' * 50)
f_1.seek(0)  # 回归鼠标位置
f_0 = open('信息表.txt', 'w', encoding='utf-8')  # 删除旧文件，创建新文件，并将修改内容加入
f_0.write(f_1.readline())  # 写文件表头
for s in id_all.values():  # 将dict内容转化为文件
    content = ''
    for l_ in s.values():
        content = content + l_ + ' '
    content = content.strip()
    f_0.write(content + ' end')
    f_0.write('\n')
f_0.close()
f_1.close()
os.remove('信息表_backup.txt')  # 删除备份文件
