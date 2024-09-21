"""
                    struct练习
"""
import struct
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ADDR = ('127.0.0.1', 10086)
while True:
    list_ = []
    for i in ('学生的编号是：', '学生的姓名是：', '学生的成绩是', '学生的年龄是：'):
        data = input(f'{i}:>')
        if data.isnumeric():
            data = int(data)
        elif data.isalpha():
            data += (10 - len(str(data))) * ' '
            data = data.encode()
        else:
            data = float(data)
        list_.append(data)
    s.sendto(struct.pack('i10sfi', *list_), ADDR)
