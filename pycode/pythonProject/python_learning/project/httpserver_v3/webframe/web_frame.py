"""
            web_frame
"""
import socket
import select
import json
from urls import *
from settings import *


class WebFrameServer:
    # 实例化变量
    def __init__(self):
        self.__sock = socket.socket()
        self.__set_sock()
        # select各个io使用的列表
        self.__rlist = [self.__sock]
        self.__wlist = []
        self.__xlist = []

    # 设置服务套接字
    def __set_sock(self):
        self.__sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, DEBUG)
        self.__sock.bind(ADDR)
        self.__sock.listen(3)

    # 处理客户端请求
    def __handle(self, sock):
        data = sock.recv(1024 ** 3).decode('gbk')
        if not data:
            return
        data = json.loads(data)
        result = self.__deal_request(data)
        result = json.dumps(result)
        sock.send(result.encode('gbk'))
        # 移除关注，防止因为持续连接导致错误
        self.__rlist.remove(sock)

    # 获取响应内容
    def __get_server(self, info):
        for rq, rp in urls_list:
            # 判断是否在路由列表中
            if rq == info:
                return {'info_type': 200, 'info': rp()}
        # 返回错误提示
        return {'info_type': 404, 'info': self.__server_miss()}

    # 处理请求，返回响应
    def __deal_request(self, request):
        # 处理get请求
        if request['info_type'] == 'GET':
            # 处理html请求
            if request['info'][-5::] == '.html':
                return self.__get_html(request)
            # 处理请求根目录
            elif request['info'] == '/':
                return self.__get_html({'info': r'\python_syntax_learning_process_oriented.html'})
            else:
                return self.__get_server(request['info'])
        elif request['info_type'] == 'POST':
            pass
        else:
            return self.__server_miss()

    # 获取响应的网页
    def __get_html(self, request):
        # 组合得到地址
        file_path = PATH + rf"\{request['info'][1:]}"
        # 打开文件，防止报错，并返回错误网页
        try:
            with open(file_path, encoding='utf8') as f:
                return {'info_type': 200, 'info': f.read()}
        except FileNotFoundError:
            return self.__server_miss()

    # 错误提示，返回错误网页
    @staticmethod
    def __server_miss():
        file_path = PATH + r'\respond.html'
        with open(file_path, encoding='gbk') as f:
            return f.read()

    # 主服务
    def run(self):
        while True:
            try:
                # 返回准备好的io
                rs, ws, xs = select.select(self.__rlist, self.__wlist, self.__xlist)
                for item in rs:
                    # 服务端套接字
                    if item is self.__sock:
                        print('Listen the port 10081...')
                        conn, addr = item.accept()
                        print('Connect from:', addr)
                        self.__rlist.append(conn)
                    # 客户端套接字
                    else:
                        self.__handle(item)
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(e)


if __name__ == '__main__':
    wf = WebFrameServer()
    wf.run()
