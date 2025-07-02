codebook = tuple('gKaPWxEQft')
print('密码表是', codebook, sep='')
deal = input('请输入加密字符串：')
re = ''
for i in deal:
    try:
        re += str(codebook.index(i))
    except Exception:
        re += '?'
print(re)
