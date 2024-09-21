"""
                            struct练习
"""
import struct
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('localhost', 10086))
with open('stu_info.txt', 'a') as file_stu_info:
    while True:
        data, addr = s.recvfrom(1024)
        dt_unpack = struct.unpack('i10sfi', data)
        for i in dt_unpack:
            if isinstance(i, bytes):
                file_stu_info.write(i.decode())
            else:
                file_stu_info.write(str(i))
            file_stu_info.write(' ')
        file_stu_info.write('\n')
        file_stu_info.flush()
