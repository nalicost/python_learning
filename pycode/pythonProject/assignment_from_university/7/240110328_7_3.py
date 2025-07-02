import re
decrypt_dict = {'xswl': '笑死我了', 'dbq': '对不起', 'cxk': '蔡徐坤', '3q': '谢谢', '88': '拜拜', 'v5': '威武'}
lag = input('请输入黑话>:')
result = re.findall(r'(xswl)|(dbq)|(cxk)|(3q)|(88)|(v5)', lag, flags=re.IGNORECASE)
for item in result:
    for obj in item:
        if obj:
            lag = lag.replace(obj, decrypt_dict[obj.lower()])
print(lag)
