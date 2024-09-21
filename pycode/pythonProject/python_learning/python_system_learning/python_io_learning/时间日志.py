"""
                            记录时间的日志
"""
import time
file = open('time_record.txt', 'a+')
file.seek(0)
line_list = file.readlines()
n = 1 if not line_list else int(line_list[-1][0]) + 1
while True:
    time.sleep(1)
    time_tuple = time.localtime(time.time())
    file.write(f'{n} ')
    file.write(time.strftime('%Y-%m-%d %H:%M:%S', time_tuple) + '\n')
    n += 1
