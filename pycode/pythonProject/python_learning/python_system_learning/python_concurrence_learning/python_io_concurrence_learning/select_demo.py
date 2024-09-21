"""
                                    select实现io多路复用demo
"""
from select import *
from socket import *
ADDR = ('127.0.0.1', 10086)
s = socket()
s.bind(ADDR)
s.listen(5)
read_list, write_list, xlist = [s], [], []
# select中各个类型的io需自己创建列表存储
while True:
    rs, ws, xs = select(read_list, write_list, xlist)
    # 用创建的列表放入其中，不然无法更新关注io
    for item in rs:
        if item is s:
            conn, addr = s.accept()
            print('Connected by', addr)
            read_list.append(conn)
        else:
            data = item.recv(1024)
            if not data:
                continue
            print(data.decode())
            write_list.append(item)
    for item in ws:
        item.send(b'Hello')
        write_list.remove(item)
    for item in xs:
        pass


# 适用于windows，linux，unix，但是windows只能监控套接字，而linux可以监控所有文件描述
