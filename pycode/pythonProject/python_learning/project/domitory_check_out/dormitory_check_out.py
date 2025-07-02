"""
                        寝室记账
"""
import pymysql
import datetime
from config import *
db, cur = None, None


# 判断数据是否符合要求
def judge_data(fun, msg, args):
    result = fun(*args)
    if result:
        return True, result
    return False, msg


# 判断函数是否要传入参数
def parameter_judge(args, fun):
    if args:
        return fun(*args)
    else:
        return fun()


# 单独获取输入
def single_input(msg, args=None):
    if args:
        display_info(args)
    choice = input(f'{msg}:>')
    return choice


# 服务选择输入获取
def server_input():
    choice_server = single_input('请选择需要的服务')
    result_judge = judge_data(lambda i: i.isdigit() and 1 <= int(i) <= 4, '请输入符合要求的数字', (choice_server,))
    return choice_server, result_judge


# 展示服务列表
def display_server():
    print('你处在第一层菜单'.center(50, '='))
    print("""
        1) 增加账单
        2) 删除账单
        3) 查看账单
        4) 查看当前轮次未付帐
        """)
    print('欢迎使用'.center(50, '='))


# 展示元组中信息
def display_info(tuple_):
    for i in range(len(tuple_)):
        print(f'{i}:{tuple_[i]}')


# 数据表中增加数据
def add_():
    choice_list = [None, None, None]
    input_tuple = (('客户', CLIENT, 'lambda i: i.isdigit() and 0 <= int(i) <= len(CLIENT) - 1'),
                   ('账单类型', TYPE, 'lambda i: i.isdigit() and 0 <= int(i) <= len(TYPE) - 1'),
                   ('金额', None,  'lambda i: i.isdigit() and int(i) > 0'))
    add_data = get_multi_input(choice_list, input_tuple)
    n = sql_language(add_data, 'add')
    print()
    print(f'添加{n}条记录成功'.center(50, '-'))


# 获取多条输入
def get_multi_input(choice_list, input_tuple):
    while True:
        for item in range(len(input_tuple)):
            choice_list[item] = single_input(input_tuple[item][0], input_tuple[item][1])
            judge_result = judge_data(eval(input_tuple[item][2]), '请输入符合要求的数字', (choice_list[item], ))
            if not judge_result[0]:
                print(judge_result[1])
                break
        else:
            return choice_list


# 删除数据表数据
def delete_():
    choice_list = [None, None]
    input_tuple = (('客户', CLIENT, 'lambda i: i.isdigit() and 0 <= int(i) <= len(CLIENT) - 1'),
                   ('id', None, 'lambda i: i.isdigit() and int(i) > 0'))
    delete_data = get_multi_input(choice_list, input_tuple)
    n = sql_language(delete_data, 'delete')
    print()
    print(f'删除{n}条记录成功'.center(50, '-'))


# 展示个人账单数据
def show_():
    choice_list = [None, None]
    input_tuple = (('客户', CLIENT, 'lambda i: i.isdigit() and 0 <= int(i) <= len(CLIENT) - 1'),
                   ('账单类型', TYPE, 'lambda i: i.isdigit() and 0 <= int(i) <= len(TYPE) - 1'))
    delete_data = get_multi_input(choice_list, input_tuple)
    n, msg = sql_language(delete_data, 'show')
    print(f'有{n}条记录'.center(50, '-'))
    show_msg(msg)
    print('end'.center(50, '-'))


# 展示账单数据信息
def show_msg(msg):
    re = ''
    for item in msg:
        for obj in item:
            if isinstance(obj, int) or isinstance(obj, datetime.datetime):
                re += str(obj)
            else:
                re += obj
    print(re)


# 展示本轮次未支付账单人员
def select_():
    choice_list = [None]
    re_list = []
    input_tuple = (('账单类型', TYPE, 'lambda i: i.isdigit() and 0 <= int(i) <= len(TYPE) - 1'), )
    select_request = get_multi_input(choice_list, input_tuple)
    get_all_record_len(re_list, select_request)
    print(''.center(50, '-'))
    print('本轮次未支付账单的有：', end='')
    seek_person_need(re_list)
    print()
    print('end'.center(50, '-'))


# 查找本轮次未支付账单的人逻辑处理
def seek_person_need(re_list):
    for index_ in range(len(re_list)):
        # 如果四个人支付次数一样
        if len(set([i[0] for i in re_list])) == 1:
            print(CLIENT[int(re_list[index_][1])], end=' ')
        try:
            # 支付次数不一样，只要小于等于-1，就说明有少付的次数
            if re_list[index_][0] - re_list[index_ + 1][0] <= -1:
                print(CLIENT[int(re_list[index_][1])], end=' ')
        except IndexError:
            return


# 获取一个人所有记录的长度
def get_all_record_len(re_list, select_request):
    for item in range(len(CLIENT)):
        request_list = [item] + select_request
        n, msg = sql_language(request_list, 'show')
        re_list.append((n, item))


# 父类
def sql_language(data_deal, sql_request):
    return sql_request_dict[sql_request](data_deal)


# 子类，完成sql加入的语句
def sql_add(data_deal):
    sql = (r"insert into %s (type_consume, cost) values ('%s', %s)"
           % (CLIENT[int(data_deal[0])], TYPE[int(data_deal[1])], data_deal[2]))
    try:
        cur.execute(sql)
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
    return 1



# 子类，完成sql删除的语句
def sql_delete(data_deal):
    sql = r"delete from %s where id = %s" % (CLIENT[int(data_deal[0])], data_deal[1])
    try:
        cur.execute(sql)
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
    return 1


# 子类，完成sql检索的语句
def sql_show(data_deal):
    sql = r"select * from %s where type_consume = '%s'" % (CLIENT[int(data_deal[0])], TYPE[int(data_deal[1])])
    cur.execute(sql)
    result = cur.fetchall()
    return len(result), result


# 连接mysql
def connect_mysql():
    global db, cur
    db = pymysql.connect(host=HOST, port=PORT, user=USER_NAME, password=PASSWORD, database=DATABASE, charset=CHARSET)
    cur = db.cursor()


# 主服务函数
def server():
    display_server()
    choice_server, result_judge = server_input()
    if result_judge[0]:
        dict_server[choice_server]()
    else:
        print(result_judge[1])


# 启动程序
def main():
    while True:
        connect_mysql()
        server()


# 获取服务对应方法
dict_server = {'1': add_, '2': delete_, '3': show_, '4': select_}
# 获取对应sql语句方法
sql_request_dict = {'add': sql_add, 'delete': sql_delete, 'show': sql_show}


main()
