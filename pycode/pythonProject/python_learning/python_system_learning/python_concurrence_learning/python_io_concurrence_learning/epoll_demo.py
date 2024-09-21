"""
                poll实现io多路复用demo
"""
from socket import *
from select import *
ADDR = ("127.0.0.1", 10086)
s = socket()
s.bind(ADDR)
s.listen(5)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
ep = epoll()
ep.register(s, EPOLLIN | EPOLLERR)
io_dict = {s.fileno(): s}
while True:
    event_list = ep.poll()
    for file_no, event in event_list:
        print(event_list)
        io_ = io_dict[file_no]
        if io_ is s:
            conn, addr = io_dict[file_no].accept()
            print("Connection from", addr)
            ep.register(conn, EPOLLIN | EPOLLERR)
            io_dict[conn.fileno()] = conn
        elif event & EPOLLIN:
            data = io_.recv(1024)
            if not data:
                ep.unregister(io_)
                io_.close()
                del io_dict[file_no]
                continue
            print(data.decode())
            ep.register(io_, EPOLLOUT)
        elif event & EPOLLOUT:
            io_.send(b"Hello")
            ep.unregister(io_)
            ep.register(io_, EPOLLIN)
