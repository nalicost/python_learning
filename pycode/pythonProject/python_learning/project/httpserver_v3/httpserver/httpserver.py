"""
                httpserver
"""
import socket
import threading
import re
import json
from config import *


class Httpserver:
    # 实例化对象
    def __init__(self):
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__set_sock()

    # 设置服务端套接字
    def __set_sock(self):
        self.__sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, DEBUG)
        self.__sock.bind(ADDR_hp)
        self.__sock.listen(3)

    # 连接处理应用
    @staticmethod
    def __connect_web_frame():
        socket_server = socket.socket()
        socket_server.connect(ADDR_wf)
        return socket_server

    # 生成响应
    @staticmethod
    def __response(data):
        data = json.loads(data)
        response = rf"HTTP/1.1 {data['info_type']}" + '\n\r'
        response += '\n\r'
        response += rf"{data['info']}"
        return response

    # 处理网页请求
    def __handle(self, conn):
        while True:
            data = conn.recv(1024 ** 3).decode('gbk')
            if not data:
                break
            data_dict = re.search(r'(?P<info_type>\S+) (?P<info>\S+) ', data).groupdict()
            # 生成json格式的内容以完成传输协议
            rq_info = json.dumps(data_dict)
            result = self.__deal_request(rq_info)
            conn.send(result.encode('gbk'))

    # 向处理应用发送处理内容
    def __deal_request(self, request):
        sock_server = self.__connect_web_frame()
        sock_server.send(request.encode())
        data = sock_server.recv(1024 ** 3).decode('gbk')
        return self.__response(data)

    # 主服务
    def server_forever(self):
        while True:
            try:
                print('Listen the port 10086...')
                conn, addr = self.__sock.accept()
                print('Connect from:', addr)
                # 多线程并发
                handle_thread = threading.Thread(target=self.__handle, args=(conn, ), daemon=True)
                handle_thread.start()
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(e)


if __name__ == '__main__':
    hp = Httpserver()
    hp.server_forever()
