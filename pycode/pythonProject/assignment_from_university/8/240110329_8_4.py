import string
import random
ls = list(string.ascii_lowercase + string.digits + string.ascii_uppercase)
for i in range(10):
    print(f'生成的第{i + 1}个8位数字密码为：', ''.join(random.sample(ls, 8)))
