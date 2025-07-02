# -*- encoding:gbk -*-
"""
                本模块为电子词典服务端的业务逻辑模块，其中包含请求响应的处理与数据库调取逻辑和相关模型的联动
"""
from electronic_dictionary_server_database_bll import *
import socket
import threading


# 继承线程类，使得可以直接调用start来实现创建进程
class CommunicationAgreementController(threading.Thread):
    """
                    网络传输协议逻辑类
    """
    # 将运行线程加入，回收线程，释放资源
    threading_list = []

    def __init__(self, addr=('127.0.0.1', 10090), socket_target=None):
        """
                    初始化实例变量
        :param addr: tuple类型，服务端主机绑定的地址
        :param socket_target: default：None；传入的客户端套接字
        """
        super().__init__()
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__addr = addr
        self.__socket_client = socket_target
        # 用来存储连接客户端用户的名字
        self.__user = None
        # 用来存储封装各个服务
        self.__service_dict = {'L': self.__login, 'R': self.__register, 'E': self.__exit,
                               'S': self.__seek_word, 'H': self.__show_history, 'Q': self.__quit}
        # 组合复用数据库调用逻辑模块
        self.database_controller = DatabaseController()

    def __set_server_sock(self):
        """
                    启动网络服务
        """
        self.__socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.__socket.bind(self.__addr)
        self.__socket.listen(3)

    def __handle_rq(self):
        """
                    处理请求，调用选择服务方法
        """
        self.__choice_service()

    def __send_rp(self, rq_content, rq_content_type):
        """
                    发送响应
        :param rq_content: 响应的具体内容
        :param rq_content_type: str类型，响应的类型
        """
        # 封装进网络传输协议类中
        rq_ = CommunicationAgreementModel(rq_content, rq_content_type)
        # 返回字符串类型，进行传输
        rq_ = rq_.__repr__()
        self.__socket_client.send(rq_.encode('gbk'))

    def __choice_service(self):
        """
                    服务选择方法
        """
        # 接收客户端的请求
        data = self.__socket_client.recv(1024).decode('gbk')
        # 断开连接，则退出线程
        if not data:
            raise BrokenPipeError
        # 将收到内容依照网络传输协议解析
        rq_ = eval(data)
        # 根据请求类型，调用函数
        self.__service_dict[rq_.content_type](rq_)

    def __login(self, rq_target):
        """
                    登录方法
        :param rq_target:请求对象
        """
        # 获取请求内容，并调用数据库逻辑模块获得处理结果
        content_re, content_state = self.database_controller.login(rq_target.content)
        # 获取成功，则添加用户
        if content_re:
            self.__user = rq_target.content[0]
        # 调用响应发送方法
        self.__send_rp(content_re, content_state)

    def __register(self, rq_target):
        """
                    注册方法
        :param rq_target:请求对象
        """
        content_re, content_state = self.database_controller.register(rq_target.content)
        self.__send_rp(content_re, content_state)

    def __exit(self, *args):
        """
                    退出方法
        :param args:多余的无用参数
        """
        # 报错退出线程
        raise BrokenPipeError

    def __seek_word(self, rq_target):
        """
                    查找单词方法
        :param rq_target:请求对象
        """
        # 获取请求内容，并调用数据库查词逻辑获取处理结果
        content_re, content_state = self.database_controller.seek_word(rq_target.content, self.__user)
        # 调用响应发送方法
        self.__send_rp(content_re, content_state)

    def __show_history(self, rq_target):
        """
                    查看历史记录方法
        :param rq_target:请求对象
        """
        # 获取请求内容，并调用数据库查词逻辑获取处理结果
        content_re, content_state = self.database_controller.show_history(rq_target.content, self.__user)
        # 调用响应发送方法
        self.__send_rp(content_re, content_state)

    def __quit(self, *args):
        """
                    登录方法
        :param args:多余的参数
        """
        # 用户退出，不关闭线程，但将用户设置为空
        self.__user = None

    def run(self):
        """
                    线程处理客户端请求
        """
        # 循环接收客户端请i去
        while True:
            try:
                self.__handle_rq()
            # 报错退出
            except BrokenPipeError:
                break

    def main(self):
        """
                    主函数
        """
        # 设置网络服务
        self.__set_server_sock()
        # 创建并启动线程回收方法，并使得主线程退出，其一起退出
        handle_t = threading.Thread(target=threading_handle, daemon=True)
        handle_t.start()
        # 循环接收客户端连接
        while True:
            try:
                socket_client, addr = self.__socket.accept()
                print('Connect from', addr)
                # 为客户端启用专属线程
                thread_client = CommunicationAgreementController(socket_target=socket_client)
                thread_client.start()
                # 在回收线程中增加创建线程
                CommunicationAgreementController.threading_list.append(thread_client)
            # 退出服务器
            except KeyboardInterrupt:
                break
            # 防止服务器异常退出
            except Exception as e:
                print(e)


def threading_handle():
    """
            线程回收函数
    """
    # 死循环处理
    while True:
        # 遍历线程回收列表
        for i in CommunicationAgreementController.threading_list:
            # 判断线程是否已完成
            if not i.is_alive():
                # 删除已完成线程
                CommunicationAgreementController.threading_list.remove(i)
            # 回收线程
            i.join(20)


if __name__ == '__main__':
    test_agreement = CommunicationAgreementController()
    test_agreement.main()

