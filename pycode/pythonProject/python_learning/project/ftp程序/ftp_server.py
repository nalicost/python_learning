"""
                        ftp程序服务端
"""
from socket import *
from multiprocessing import Process
from threading import Thread
from time import sleep


class MultiprocessHelper:
    """
            多进程管理小帮手
    """
    __process_list = []
    # 存储创建进程

    def __init__(self, target=None, args=(), kwargs=()):
        """
        :param target: 目标函数
        :param args: tuple，位置传参
        :param kwargs: dict，关键字传参
        """
        self.__target = target
        self.process_ = Process(target=target, args=args, kwargs=kwargs)

    @classmethod
    def zombie_handle_thread_start(cls):
        __thread = Thread(target=cls.zombie_handle, daemon=True)
        __thread.start()

    @classmethod
    def zombie_handle(cls):
        """
                    僵尸进程处理
        """
        while True:
            # 循环遍历进程列表
            for item in range(len(cls.__process_list)):
                cls.__process_list[item].join(3)
                # 回收进程，并超时检测
                if not cls.__process_list[item].is_alive():
                    # 销毁关闭进程
                    del cls.__process_list[item]

    def __set_process(self, value):
        """
                    进程写入
        :param value: 进程对象
        """
        if self.__target is not None:
            self.__process = value
            self.__process.start()
            # 设置进程并启用进程
            MultiprocessHelper.__process_list.append(self.__process)
            # 先启动后加入进程，防止join报错

    process_ = property(None, __set_process)
    # process_设置属性只写不读


class FileModel:
    """
                文件模型
    """
    def __init__(self):
        self.file_list = self.__read_file()
        # 生成文件目录

    @staticmethod
    def __read_file():
        """
                    加载文件目录配置文件
        :return: 文件目录列表
        """
        with open('file_config.txt', 'r') as f:
            return f.readlines()

    def get_file_list(self):
        """
                    获取文件目录
        :return: list，文件目录
        """
        return self.file_list

    def add_file(self, file_name):
        """
                    增加文件目录
        :param file_name: 文件名称
        """
        self.file_list.append(file_name)
        # 增加文件名
        self.file_list.append(file_name)
        # 增加文件地址
        with open('file_config.txt', 'a') as f:
            f.write(file_name + '\n')
            # 增加文件名
            f.write(file_name + '\n')
            # 增加文件地址


class FtpServerController:
    def __init__(self):
        """
        :parameter:__addr:服务端地址
        :parameter:sock:服务端套接字
        :parameter:__dict_service:服务端服务
        :parameter:multiprocess_helper:多进程助手对象
        :parameter:file_manager:文件管理对象
        """
        self.__addr = ('127.0.0.1', 10081)
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.__dict_service = {'V': self.present_file_mena, 'D': self.send_file, 'U': self.recv_file, 'Q': self.quit}
        # 封装服务函数
        self.multiprocess_helper = MultiprocessHelper()
        self.file_manager = FileModel()

    def present_file_mena(self, sock_client, *args):
        """
                    发送文件目录
        :param sock_client: 客户端套接字
        :param args: 多余的参数
        """
        msg = (''.join(self.file_manager.get_file_list()[:-1:2]) + 'E').encode()
        sock_client.send(msg)

    def send_file(self, sock_client, target_list):
        """
                    发送文件
        :param sock_client:客户端套接字
        :param target_list: 客户端请求列表
        """
        for item in range(len(self.file_manager.get_file_list())):
            if self.file_manager.get_file_list()[item][:-1:] == target_list[1]:
                # 判断文件是否存在
                sock_client.send(b'P')
                # 发送许可响应
                sleep(0.1)
        # 循环列表检索文件
                with open(self.file_manager.get_file_list()[item + 1][:-1:], 'rb') as f:
                    for line in f:
                        sock_client.send(line)
                # 读取文件
                sock_client.send(b'E')
                # 发送文件终止响应
                break
        else:
            sock_client.send('文件不存在'.encode())
            # 发送错误信息响应

    def recv_file(self, sock_client, target_list):
        """
                        接受文件
        :param sock_client: 客户端套接字
        :param target_list: 客户端请求列表
        """
        for item in range(len(self.file_manager.get_file_list())):
            if self.file_manager.get_file_list()[item][:-1:] == target_list[1]:
                sock_client.send('文件已存在'.encode())
                # 发送文件存在错误响应
                break
        # 文件存在检测
        else:
            self.file_manager.add_file('2' + target_list[1])
            # 更改文件目录与文件目录配置文件
            sock_client.send(b'P')
            sleep(0.1)
            # 发送许可响应
            FtpServerController.write_file(sock_client, target_list)
            # 写入文件

    @staticmethod
    def write_file(sock_client, target_list):
        """
                        文件写入
        :param sock_client: 客户端套接字
        :param target_list: 客户端请求列表
        """
        with open('2' + target_list[1], 'wb') as f:
            while True:
                data = sock_client.recv(1024)
                if data.decode()[-1] == 'E':
                    # 判断文件终止响应，防止粘包
                    f.write(data[:-1:])
                    # 不写入E
                    break
                f.write(data)
            f.flush()

    def quit(self, *args):
        """
                    进程退出
        :param args: 多余的参数
        """
        raise KeyboardInterrupt

    def __my_connect(self):
        """
                    服务端连接
        """
        while True:
            try:
                c, addr = self.__sock.accept()
                print('connect from', addr)
                # 循环接受连接请求
                MultiprocessHelper(self.handle_master, (c,))
                # 创建各个客户端专属进程
                c.close()
                # 主进程关闭客户端套接字
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(e)
                continue
                # 防止服务端异常退出

    def __server_seeker(self, list_requirement, sock_client):
        """
                        服务匹配
        :param list_requirement: 客户端请求列表
        :param sock_client: 客户端套接字
        """
        self.__dict_service[list_requirement[0]](sock_client, list_requirement)
        # 获取服务处理函数

    def handle_master(self, sock_client):
        """
                    客户端请求处理
        :param sock_client: 客户端套接字
        """
        self.__sock.close()
        # 关闭服务端套接字
        while True:
            data = sock_client.recv(1024).decode()
            # 循环接收对应客户端请求
            if not data:
                # 客户端断开退出进程
                break
            list_requirement = data.split(' ')
            # 分割客户端请求
            try:
                self.__server_seeker(list_requirement, sock_client)
                # 匹配服务
            except KeyboardInterrupt:
                # 处理深层函数raise的结束错误，结束进程
                break
        sock_client.close()
        # 关闭客户端套接字

    def __set_sock(self, value):
        """
                    服务端套接字写入
        :param value: 套接字对象
        """
        self.__sock = value
        # 创建套接字
        self.__sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        # 设置端口重用
        self.__sock.bind(self.__addr)
        # 绑定服务器地址
        self.__sock.listen(5)
        # 设置监听

    def main(self):
        """
                        程序主入口
        """
        self.multiprocess_helper.zombie_handle_thread_start()
        # 启用僵尸进程处理
        self.__my_connect()
        # 建立连接

    sock = property(None, __set_sock)
    # 设置sock属性，只写


if __name__ == '__main__':
    ftp_server = FtpServerController()
    ftp_server.main()


"""
关于文件检索的优化
可以直接使用
try:
    with open(f'{filename}', 'rb'):
        ......
        ......
except FileNotFoundError:
    sock_client.send('文件不存在'.decode())
让系统自主检索


关于MultiprocessHelper的优化
可以让FtpServer直接继承Process，在run()函数中完成各个函数的调用
"""