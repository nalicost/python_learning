"""
                相比httpserver1.0增加了io并发
"""
import socket
import select


class HttpServer:
    def __init__(self, addr=('127.0.0.1', 10086), path=r'/home/nalicost/桌面/html格式'):
        self.ADDR = addr
        self.PATH = path
        self.SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.EPOLL = select.epoll()
        self.IODICT = {self.SOCK.fileno(): self.SOCK}
        self.content = []

    def server_forever(self):
        self.__set_net_link()
        self.__connection()

    def __set_net_link(self):
        self.SOCK.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.SOCK.bind(self.ADDR)
        self.SOCK.listen(5)
        self.EPOLL.register(self.SOCK, select.EPOLLIN)

    def __connection(self):
        while True:
            epoll_list = self.EPOLL.poll()
            for fd_num, event in epoll_list:
                fd = self.IODICT[fd_num]
                if fd is self.SOCK:
                    self.__io_accept()
                elif event & select.EPOLLIN:
                    self.__handle_request(fd)
                elif event & select.EPOLLOUT:
                    self.__send_respond(fd)

    def __io_accept(self):
        conn, addr = self.SOCK.accept()
        print('connect from', addr)
        self.EPOLL.register(conn, select.EPOLLIN)
        self.IODICT[conn.fileno()] = conn

    def __handle_request(self, io_):
        try:
            rq_list = self.__receive_request(io_)
            self.__request_identify(rq_list)
            self.EPOLL.unregister(io_)
            self.EPOLL.register(io_, select.EPOLLIN | select.EPOLLOUT)
        except ValueError:
            pass

    def __request_identify(self, rq_list):
        if rq_list[0] == 'GET':
            self.__get_file(rq_list)
        else:
            self.__open_file('/home/nalicost/桌面/html格式/respond.html')

    def __get_file(self, rq_list):
        if rq_list[1] == '/':
            self.__open_file()
        elif rq_list[1][-1:-4] != 'html':
            self.__open_file('/home/nalicost/桌面/html格式/respond.html')
        else:
            try:
                self.__open_file(self.PATH + rq_list[1])
            except FileNotFoundError:
                self.content = ['File Not Found']

    def __receive_request(self, io_):
        data = io_.recv(1024).decode()
        print(data)
        self.__end_connect(data, io_)
        rq_list = data.split(' ')
        return rq_list

    def __open_file(self, path_=r'/home/nalicost/桌面/html格式/python_syntax_learning_process_oriented.html'):
        with open(path_) as f:
            self.content = f.readlines()

    def __end_connect(self, data, io_):
        if not data:
            self.EPOLL.unregister(io_)
            del self.IODICT[io_.fileno()]
            io_.close()
            raise ValueError

    def __send_respond(self, io_):
        data = 'HTTP/1.1 200 OK\n\rContent-Type:text/html\n\r\n\r' + ''.join(self.content)
        print(data)
        io_.send(data.encode('gbk'))
        self.EPOLL.unregister(io_)
        del self.IODICT[io_.fileno()]
        io_.close()


if __name__ == '__main__':
    server = HttpServer()
    server.server_forever()
