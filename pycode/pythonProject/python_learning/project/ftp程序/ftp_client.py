"""
                ftp程序客户端
"""
from socket import *
import os
from time import sleep


class FptClientView:
    def __init__(self):
        """
        parameter: __sock: 客户端套接字
        parameter: __addr: 服务端地址
        parameter: __dict_service: 可选择的服务函数封装
        """
        self.__sock = socket(AF_INET, SOCK_STREAM)
        self.__addr = ('127.0.0.1', 10081)
        self.__dict_service = {1: self.__get_file_msg, 2: self.__dl_file, 3: self.__ul_file, 4: self.__quit}

    def __my_connect(self):
        """
                    与服务端建立连接
        """
        self.__sock.connect(self.__addr)

    @staticmethod
    def __int_input_judge(choose, fun):
        """
                    str转int
        :param choose: str，需转化的字符串
        :param fun: def，条件判断语句
        :return: int，转化后的数字或者表示false的0
        """
        if fun(choose):
            return int(choose)
        print('请输入指定的数字')
        return 0

    @staticmethod
    def __show_mena():
        """
                菜单展示
        """
        print("""
        1 ： 查看已存储文件
        2 ： 下载指定文件
        3 ： 上传指定文件
        4 ： 退出程序  
        """)

    def __select_service(self, choose_item):
        """
                    功能选择
        :param choose_item: int，选择的功能
        """
        self.__dict_service[choose_item]()
        # 通过字典封装各个函数，用字典键值对的方式替代if-elif分支结构

    def __get_file_msg(self):
        """
                    获取文件请求
        """
        self.__request_respond('V')
        # 组织并发送请求
        response_msg_list = []
        # 存放所有接收信息
        while True:
            data = self.__sock.recv(1024).decode()
            response_msg_list.append(data)
            if data[-1] == 'E':
                # 判断接受信息的终止符号，防止粘包
                break
        print(''.join(response_msg_list)[:-1:1], end='')
        # 合并接收信息内容，打印

    def __dl_file(self):
        """
                    下载文件请求
        """
        while True:
            file_name = input('你要下载的文件是:>')
            if self.__request_respond('D', file_name, lambda: self.__sock.recv(1024).decode()):
                # 判断服务端是否接受请求
                break
        with open(f'''{'1' + file_name}''', 'wb') as f:
            # 接收写入文件内容
            while True:
                data = self.__sock.recv(1024)
                if data.decode()[-1] == 'E':
                    # 判断接受信息的终止符号，防止粘包
                    f.write(data[:-1:])
                    # 不写入最后一个表示终止的符号
                    break
                f.write(data)
        f.flush()

    def __ul_file(self):
        while True:
            file_name = input('你要上传的文件是:>')
            if not os.path.exists(file_name):
                # 判断文件是否存在
                print('文件不存在')
                continue
            elif self.__request_respond('U', file_name, lambda: self.__sock.recv(1024).decode()):
                # 判断服务端是否接受请求
                break
        with open(f'{file_name}', 'rb') as f:
            # 打开文件读取文件内容
            for line in f:
                self.__sock.send(line)
            sleep(0.1)
            self.__sock.send(b'E')
            # 发送文件终止响应

    def __quit(self):
        """
                    退出请求
        """
        self.__sock.send(b'Q')
        # 组织并发送退出请求
        self.__sock.close()
        # 关闭客户端套接字
        exit()
        # 退出程序

    def __request_respond(self, req, msg='', fun=lambda: 'P'):
        """
                        请求与响应的组织发送与接收解析
        :param req: str，请求头
        :param msg: str，请求内容
        :param fun: def，响应解析函数
        :return: bool
        """
        request_msg = f'{req} {msg}'.encode()
        # 组织请求
        self.__sock.send(request_msg)
        info = fun()
        if info == 'P':
            # 判断服务端是否接受请求
            print('允许操作')
            return True
        print(info)
        # 打印错误原因
        return False

    def __choose_input(self):
        """
                    选择录入
        """
        choose = input('你选择的服务是:>')
        choice = FptClientView.__int_input_judge(choose, lambda x: x in ('1', '2', '3', '4'))
        # choose由str转int
        if choice:
            self.__select_service(choice)
            # 调用服务选择

    def main(self):
        """
                    程序入口
        """
        self.__my_connect()
        # 建立连接
        while True:
            FptClientView.__show_mena()
            # 展示服务
            self.__choose_input()
            # 服务选择


if __name__ == '__main__':
    fpt_client = FptClientView()
    fpt_client.main()
