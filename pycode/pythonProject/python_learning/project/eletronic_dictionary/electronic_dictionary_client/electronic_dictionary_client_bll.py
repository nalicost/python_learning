# -*- encoding:gbk -*-
"""
            本模块为电子词典客户端的业务逻辑模块包含请求响应的处理与ui和model模块的联动
"""
from electronic_dictionary_client_model import *
import socket
# 服务端地址
ADDR = ('127.0.0.1', 10090)


class CommunicationAgreementController:
    """
                传输协议逻辑类
    """
    def __init__(self):
        """
                初始化实例变量
        """
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def inet_connect(self):
        """
                建立网络连接
        """
        self.__socket.connect(ADDR)

    def __handle_rp(self):
        """
                处理响应
        """
        # 接收服务端响应
        data = self.__socket.recv(1024).decode('gbk')
        # 解析协议
        rp_ = eval(data)
        # 处理返回协议内容
        return rp_.content_type == 'T', rp_.content

    def __send_rq(self, rq_content, rq_content_type):
        """
                发送请求
        :param rq_content:请求具体内容
        :param rq_content_type:str类型，请求类型
        """
        # 使用传输协议模块封装
        rq_ = CommunicationAgreementModel(rq_content, rq_content_type)
        rq_ = rq_.__repr__()
        self.__socket.send(rq_.encode('gbk'))

    def login(self, name, password):
        """
                登录方法
        :param name:str类型，用户姓名
        :param password:str类型，用户密码
        """
        # 调用请求发送与响应处理方法来从服务端获取处理结果
        self.__send_rq((name, password), 'L')
        return self.__handle_rp()

    def register(self, name, password):
        """
                        注册方法
        :param name:str类型，用户姓名
        :param password:str类型，用户密码
        """
        # 调用请求发送与响应处理方法来从服务端获取处理结果
        self.__send_rq((name, password), 'R')
        return self.__handle_rp()

    def exit(self):
        """
                        退出方法
        """
        # 调用请求发送通知服务端客户端退出
        self.__send_rq(None, 'Q')
        raise KeyboardInterrupt

    def seek_word(self, word_seek):
        """
                        注册方法
        :param word_seek:str类型，要查找的单词
        """
        # 调用请求发送与响应处理方法来从服务端获取处理结果
        self.__send_rq(word_seek, 'S')
        return self.__handle_rp()

    def show_history(self, bool_pretty_one):
        """
                        注册方法
        :param bool_pretty_one:str类型，'T' or 'F'
        """
        # 调用请求发送与响应处理方法来从服务端获取处理结果
        self.__send_rq(bool_pretty_one == 'T', 'H')
        return self.__handle_rp()

    def quit(self):
        """
                        退出方法
        """
        # 调用请求发送来通知服务端用户退出的消息
        self.__send_rq(None, 'Q')


if __name__ == '__main__':
    test_agreement = CommunicationAgreementController()
    test_agreement.inet_connect()
