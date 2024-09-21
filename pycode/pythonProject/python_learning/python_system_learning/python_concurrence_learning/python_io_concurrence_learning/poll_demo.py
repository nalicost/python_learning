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
p = poll()
p.register(s, POLLIN | POLLERR)
io_dict = {s.fileno(): s}
while True:
    event_list = p.poll()
    for file_no, event in event_list:
        print(event_list)
        io_ = io_dict[file_no]
        if io_ is s:
            conn, addr = io_dict[file_no].accept()
            print("Connection from", addr)
            p.register(conn, POLLIN | POLLERR)
            io_dict[conn.fileno()] = conn
        elif event & POLLIN:
            data = io_.recv(1024)
            if not data:
                p.unregister(io_)
                io_.close()
                del io_dict[file_no]
                continue
            print(data.decode())
            p.register(io_, POLLOUT)
        elif event & POLLOUT:
            io_.send(b"Hello")
            p.unregister(io_)
            p.register(io_, POLLIN)
