# -*- encoding:gbk -*-
"""
            本模块为电子词典服务端的数据模型，其中包含传输协议数据模型和sql语句数据模型
"""
import pymysql


class CommunicationAgreementModel:
    """
                传输协议类
    """
    def __init__(self, content, content_type):
        """
                初始化实例变量
        :param content:传输内容
        :param content_type:请求或响应的类型
        """
        self.content = content
        self.content_type = content_type

    def __repr__(self):
        """
                返回字符串形式的类
        """
        # 如果为字符串再加引号，防止exal时出错
        if isinstance(self.content, str):
            return f"CommunicationAgreementModel('{self.content}', '{self.content_type}')"
        else:
            return f"CommunicationAgreementModel({self.content}, '{self.content_type}')"


class SQLLanguageModel:
    """
                sql语句模型
    """
    def __init__(self, host='localhost', port=3306, user='root',
                 password='Zjy20170132', database='dict', charset='utf8'):
        """
                初始化实例变量
        :param host:str类型，mysql的主机地址
        :param port:int类型，mysql所在主机上占用的端口号
        :param user:str类型，mysql的用户名
        :param password:str类型，mysql用户的对应密码
        :param database:str类型，mysql中所使用的数据库
        :param charset:str类型，mysql中所使用的数据库的字符编码方式
        """
        self.__db = pymysql.connect(host=host,
                                    port=port,
                                    user=user,
                                    password=password,
                                    database=database,
                                    charset=charset)
        self.__cur = self.__db.cursor()

    def exception_deal_and_commit(self, func_old, *args, **kwargs):
        """
                写操作的提交与错误处理
        :param func_old:函数，需要被传入的方法
        :return:错误对象
        """
        # 使用错误处理来防止数据库由于错误录入数据而出现问题
        try:
            func_old(*args, **kwargs)
        except Exception as e:
            # 回滚数据库
            self.__db.rollback()
            return e
        # 将写操作提交数据库
        self.__db.commit()

    def insert_data(self, list_target, tuple_field, tuple_data_type, table):
        """
                向数据库的表中插入数据
        :param list_target:list类型，需要存入的一个或多个记录，每一个记录使用元组依序封装
        :param tuple_field:tuple类型，插入数据对应的字段
        :param tuple_data_type:tuple类型，插入数据对应字段的数据类型
        :param table:str类型，需要操作的表
        """
        # 将各个元组转化为字符串来符合sql格式
        str_data_type, str_field = self.__join_list_for_sql(tuple_data_type, tuple_field)
        # 循环每个记录，使每个记录被写入数据库
        for item in range(len(list_target)):
            # 插入记录的sql语句生成
            sql = "insert into %s (%s) values (%s)" % (table, str_field, str_data_type)
            sql = sql % list_target[item]
            # 执行sql语句
            self.__cur.execute(sql)

    @staticmethod
    def __join_list_for_sql(*args):
        """
                sql格式转化器
        :param args:需要转化sql格式的内容，其中元素为tuple类型
        :return:转化后的列表
        """
        # 转化为列表，方便修改
        args = list(args)
        # 遍历，按序转化
        for item in range(len(args)):
            # 按格式拼接字符串
            args[item] = ', '.join(args[item])
        # 返回转化后的列表
        return args

    def index_data(self, table, index_target=('*', ), index_rq=None):
        """
                数据库数据检索器
        :param table:str类型，需要操作的表
        :param index_target: tuple类型，需要返回的字段名;default:('*', )，即返回所有字段
        :param index_rq:str类型，查找数据的条件（sql格式）
        :return:查询到的内容
        """
        index_target = ', '.join(index_target)
        if not index_rq:
            # 如果没有查找条件，则不使用where语句
            sql = "select %s from %s" % (index_target, table)
        else:
            # 如果有，则使用where语句
            sql = "select %s from %s %s" % (index_target, table, index_rq)
        # 执行sql语句
        self.__cur.execute(sql)
        # 返回查找到所有的内容
        return self.__cur.fetchall()

    def create_tabel(self, table, field_tuple):
        """
                数据库表格创建器
        :param table:str类型，创建表名称
        :param field_tuple:tuple类型，创建的字段
        """
        field_tuple = self.__join_list_for_sql(field_tuple)[0]
        # 创建表格
        sql = "create table %s (%s)" % (table, field_tuple)
        # 执行sql语句
        self.__cur.execute(sql)


if __name__ == '__main__':
    mysql_test = SQLLanguageModel(database='test_database')
    # mysql_test.exception_deal_and_commit(mysql_test.create_tabel, 'test_table_1', ('id int not null', ))
    # mysql_test.exception_deal_and_commit(mysql_test.insert_data, [(1, ), (2, )], ('id', ), ('%d', ), 'test_table_1')
    # print(mysql_test.index_data('test_table_1', ('id', )))
    # print(mysql_test.index_data('test_table_1', index_rq='id = 1'))
    # test_model = CommunicationAgreementModel((1, 2), 'T')
    # test_repr =test_model.__repr__()
    # print(test_repr)
    # print(eval(test_repr).content[0])
    # mysql_test = SQLLanguageModel()
    # mysql_test.insert_data([('abb', '123')], ('name', 'password'),
    #                         ("'%s'", "'%s'"), 'user')
    # print(mysql_test.index_data('words', index_rq=f"where spell = 'apple'"))
    # mysql_test.insert_data([('apple', )], ('word',),
    #                        ("'%s'",), f'张三')
