# -*- encoding:gbk -*-
"""
                此模块为电子词典的业务逻辑，其中包含关于数据库调取的部分
"""
from electronic_dictionary_server_model import *
import datetime


class DatabaseController:
    """
                数据库调用逻辑类
    """
    def __init__(self):
        # 组合复用SQLLanguage数据模型
        self.__sql = SQLLanguageModel()

    def login(self, rq_target):
        """
                登录逻辑处理
        :param rq_target:请求具体内容
        """
        # 通过调用数据库的index函数，获得用户名对应的密码，将内容转化为sql语句并由数据库执行查找逻辑，注意值是要带引号的
        password = self.__sql.index_data('user', ('password', ), f"where name = '{rq_target[0]}'")
        # 判断密码是否存在或者密码是否正确
        if password and password[0][0] == rq_target[1]:
            msg, re = f'{rq_target[0]}登录成功', 'T'
        else:
            msg, re = f'密码或用户名不正确', 'F'
        return msg, re

    def register(self, rq_target):
        """
                        登录逻辑处理
        :param rq_target:请求具体内容
        """
        # 调用数据库查找逻辑，判断用户是否存在
        if self.__sql.index_data('user', index_rq=f"where name = '{rq_target[0]}'"):
            msg, re = '用户已存在', 'F'
        else:
            # 不存在则调用数据库添加逻辑，写入用户数据库
            self.__sql.exception_deal_and_commit(self.__sql.insert_data, [rq_target], ('name', 'password'),
                                                 ("'%s'", "'%s'"), 'user')
            # 创建用户专属子表
            self.__sql.create_tabel(f'{rq_target[0]}', ('word varchar(128) not null', 'time datetime default now()'))
            msg, re = '注册成功', 'T'
        return msg, re

    def seek_word(self, rq_target, user_name):
        """
                        登录逻辑处理
        :param rq_target:具体请求内容
        :param user_name:str类型用户姓名
        """
        # 通过调用数据库查找语句来获取单词释义
        msg = self.__sql.index_data('words', index_rq=f"where spell = '{rq_target}'")
        re = 'T'
        # 判断单词是否存在
        if msg:
            # 将单词除id外合并，返回结果
            msg = ' '.join(msg[0][1::])[:-1:]
            # 通过调用数据库添加语句，来记录用户查询记录
            self.__sql.exception_deal_and_commit(self.__sql.insert_data, [(rq_target, )], ('word', ),
                                                 ("'%s'", ), f'{user_name}')
        else:
            msg = '不存在该词汇'
        return msg, re

    def show_history(self, rq_target, user_name):
        """
                        登录逻辑处理
        :param rq_target:
        """
        msg_final = ''
        # 通过调用数据库查找逻辑，降序排列用户搜索记录
        msg = self.__sql.index_data(f'{user_name}', index_rq='order by time DESC')
        # 获取遍历长度
        len_ = 0 if not msg else 10 if rq_target and 10 < len(msg) else len(msg)
        # 遍历获取用户记录
        for item in range(len_):
            for obj in range(len(msg[item])):
                # 需使用datetime模块
                msg_final += str(msg[item][obj]) + ' '
            msg_final += '\n'
        return (msg_final, len_), 'T'

