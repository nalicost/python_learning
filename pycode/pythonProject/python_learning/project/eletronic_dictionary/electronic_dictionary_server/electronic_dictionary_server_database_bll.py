# -*- encoding:gbk -*-
"""
                ��ģ��Ϊ���Ӵʵ��ҵ���߼������а����������ݿ��ȡ�Ĳ���
"""
from electronic_dictionary_server_model import *
import datetime


class DatabaseController:
    """
                ���ݿ�����߼���
    """
    def __init__(self):
        # ��ϸ���SQLLanguage����ģ��
        self.__sql = SQLLanguageModel()

    def login(self, rq_target):
        """
                ��¼�߼�����
        :param rq_target:�����������
        """
        # ͨ���������ݿ��index����������û�����Ӧ�����룬������ת��Ϊsql��䲢�����ݿ�ִ�в����߼���ע��ֵ��Ҫ�����ŵ�
        password = self.__sql.index_data('user', ('password', ), f"where name = '{rq_target[0]}'")
        # �ж������Ƿ���ڻ��������Ƿ���ȷ
        if password and password[0][0] == rq_target[1]:
            msg, re = f'{rq_target[0]}��¼�ɹ�', 'T'
        else:
            msg, re = f'������û�������ȷ', 'F'
        return msg, re

    def register(self, rq_target):
        """
                        ��¼�߼�����
        :param rq_target:�����������
        """
        # �������ݿ�����߼����ж��û��Ƿ����
        if self.__sql.index_data('user', index_rq=f"where name = '{rq_target[0]}'"):
            msg, re = '�û��Ѵ���', 'F'
        else:
            # ��������������ݿ�����߼���д���û����ݿ�
            self.__sql.exception_deal_and_commit(self.__sql.insert_data, [rq_target], ('name', 'password'),
                                                 ("'%s'", "'%s'"), 'user')
            # �����û�ר���ӱ�
            self.__sql.create_tabel(f'{rq_target[0]}', ('word varchar(128) not null', 'time datetime default now()'))
            msg, re = 'ע��ɹ�', 'T'
        return msg, re

    def seek_word(self, rq_target, user_name):
        """
                        ��¼�߼�����
        :param rq_target:������������
        :param user_name:str�����û�����
        """
        # ͨ���������ݿ�����������ȡ��������
        msg = self.__sql.index_data('words', index_rq=f"where spell = '{rq_target}'")
        re = 'T'
        # �жϵ����Ƿ����
        if msg:
            # �����ʳ�id��ϲ������ؽ��
            msg = ' '.join(msg[0][1::])[:-1:]
            # ͨ���������ݿ������䣬����¼�û���ѯ��¼
            self.__sql.exception_deal_and_commit(self.__sql.insert_data, [(rq_target, )], ('word', ),
                                                 ("'%s'", ), f'{user_name}')
        else:
            msg = '�����ڸôʻ�'
        return msg, re

    def show_history(self, rq_target, user_name):
        """
                        ��¼�߼�����
        :param rq_target:
        """
        msg_final = ''
        # ͨ���������ݿ�����߼������������û�������¼
        msg = self.__sql.index_data(f'{user_name}', index_rq='order by time DESC')
        # ��ȡ��������
        len_ = 0 if not msg else 10 if rq_target and 10 < len(msg) else len(msg)
        # ������ȡ�û���¼
        for item in range(len_):
            for obj in range(len(msg[item])):
                # ��ʹ��datetimeģ��
                msg_final += str(msg[item][obj]) + ' '
            msg_final += '\n'
        return (msg_final, len_), 'T'

