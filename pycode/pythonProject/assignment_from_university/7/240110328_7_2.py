decrypt_dict = {'xswl': '笑死我了', 'dbq': '对不起', 'cxk': '蔡徐坤', '3q': '谢谢', '88': '拜拜', 'v5': '威武'}
lag = input('请输入带有黑话的句子以及黑化，用英文逗号分割>:')
result = lag.split(',')
str_re = result[0].replace(result[1], decrypt_dict[result[1]])
print(str_re)
