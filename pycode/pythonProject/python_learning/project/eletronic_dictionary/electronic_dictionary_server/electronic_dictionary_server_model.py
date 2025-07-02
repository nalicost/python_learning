# -*- encoding:gbk -*-
"""
            ��ģ��Ϊ���Ӵʵ����˵�����ģ�ͣ����а�������Э������ģ�ͺ�sql�������ģ��
"""
import pymysql


class CommunicationAgreementModel:
    """
                ����Э����
    """
    def __init__(self, content, content_type):
        """
                ��ʼ��ʵ������
        :param content:��������
        :param content_type:�������Ӧ������
        """
        self.content = content
        self.content_type = content_type

    def __repr__(self):
        """
                �����ַ�����ʽ����
        """
        # ���Ϊ�ַ����ټ����ţ���ֹexalʱ����
        if isinstance(self.content, str):
            return f"CommunicationAgreementModel('{self.content}', '{self.content_type}')"
        else:
            return f"CommunicationAgreementModel({self.content}, '{self.content_type}')"


class SQLLanguageModel:
    """
                sql���ģ��
    """
    def __init__(self, host='localhost', port=3306, user='root',
                 password='Zjy20170132', database='dict', charset='utf8'):
        """
                ��ʼ��ʵ������
        :param host:str���ͣ�mysql��������ַ
        :param port:int���ͣ�mysql����������ռ�õĶ˿ں�
        :param user:str���ͣ�mysql���û���
        :param password:str���ͣ�mysql�û��Ķ�Ӧ����
        :param database:str���ͣ�mysql����ʹ�õ����ݿ�
        :param charset:str���ͣ�mysql����ʹ�õ����ݿ���ַ����뷽ʽ
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
                д�������ύ�������
        :param func_old:��������Ҫ������ķ���
        :return:�������
        """
        # ʹ�ô���������ֹ���ݿ����ڴ���¼�����ݶ���������
        try:
            func_old(*args, **kwargs)
        except Exception as e:
            # �ع����ݿ�
            self.__db.rollback()
            return e
        # ��д�����ύ���ݿ�
        self.__db.commit()

    def insert_data(self, list_target, tuple_field, tuple_data_type, table):
        """
                �����ݿ�ı��в�������
        :param list_target:list���ͣ���Ҫ�����һ��������¼��ÿһ����¼ʹ��Ԫ�������װ
        :param tuple_field:tuple���ͣ��������ݶ�Ӧ���ֶ�
        :param tuple_data_type:tuple���ͣ��������ݶ�Ӧ�ֶε���������
        :param table:str���ͣ���Ҫ�����ı�
        """
        # ������Ԫ��ת��Ϊ�ַ���������sql��ʽ
        str_data_type, str_field = self.__join_list_for_sql(tuple_data_type, tuple_field)
        # ѭ��ÿ����¼��ʹÿ����¼��д�����ݿ�
        for item in range(len(list_target)):
            # �����¼��sql�������
            sql = "insert into %s (%s) values (%s)" % (table, str_field, str_data_type)
            sql = sql % list_target[item]
            # ִ��sql���
            self.__cur.execute(sql)

    @staticmethod
    def __join_list_for_sql(*args):
        """
                sql��ʽת����
        :param args:��Ҫת��sql��ʽ�����ݣ�����Ԫ��Ϊtuple����
        :return:ת������б�
        """
        # ת��Ϊ�б������޸�
        args = list(args)
        # ����������ת��
        for item in range(len(args)):
            # ����ʽƴ���ַ���
            args[item] = ', '.join(args[item])
        # ����ת������б�
        return args

    def index_data(self, table, index_target=('*', ), index_rq=None):
        """
                ���ݿ����ݼ�����
        :param table:str���ͣ���Ҫ�����ı�
        :param index_target: tuple���ͣ���Ҫ���ص��ֶ���;default:('*', )�������������ֶ�
        :param index_rq:str���ͣ��������ݵ�������sql��ʽ��
        :return:��ѯ��������
        """
        index_target = ', '.join(index_target)
        if not index_rq:
            # ���û�в�����������ʹ��where���
            sql = "select %s from %s" % (index_target, table)
        else:
            # ����У���ʹ��where���
            sql = "select %s from %s %s" % (index_target, table, index_rq)
        # ִ��sql���
        self.__cur.execute(sql)
        # ���ز��ҵ����е�����
        return self.__cur.fetchall()

    def create_tabel(self, table, field_tuple):
        """
                ���ݿ��񴴽���
        :param table:str���ͣ�����������
        :param field_tuple:tuple���ͣ��������ֶ�
        """
        field_tuple = self.__join_list_for_sql(field_tuple)[0]
        # �������
        sql = "create table %s (%s)" % (table, field_tuple)
        # ִ��sql���
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
    #                        ("'%s'",), f'����')
