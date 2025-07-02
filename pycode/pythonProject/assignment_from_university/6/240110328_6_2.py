code = ('g', 'K', 'a', 'P', 'W', 'x', 'E', 'Q', 'f', 't')
d = ''
s = input('请输入密文:')
for i in range(len(s)):
    if s[i] in code:
        p = code.index(s[i])
        d += str(p)
    else:
        d += '?'
print('明文是:', d)
