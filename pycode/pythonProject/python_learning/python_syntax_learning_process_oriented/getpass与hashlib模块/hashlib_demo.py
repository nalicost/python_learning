"""
                hashlib模块的演示
"""
import hashlib
salt = '*#?'
p = hashlib.md5()
str_ = 'abc123'
p.update(str_.encode())
print(p.hexdigest())
# 加盐加密
p.update((str_ + salt).encode())
print(p.hexdigest())
