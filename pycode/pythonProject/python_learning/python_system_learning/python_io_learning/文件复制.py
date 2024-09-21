"""
                        将输入文件保存至当前目录下
"""
file_copy, file_new_name = input('你需要copy文件的绝对路径是:>'), input('新文件的名字是:>')
try:
    file_read = open(f'{file_copy}', 'rb')
except FileNotFoundError:
    print('文件不存在')
else:
    file_new = open(f'{file_new_name}', 'wb')
    temp = file_read.read()
    file_new.write(temp)
    file_read.close()
    file_new.close()
