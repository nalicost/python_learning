# -*- encoding:gbk -*-
"""
                    ������ϰ�����ڣ�linux��
"""
import os
pid = os.fork()
if pid < 0:
    print('false')
elif pid == 0:
    print('new process')
else:
    print('old process')
print('process over')
