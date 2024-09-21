import string
original_text=string.ascii_lowercase#原文字
print(original_text)
cooperate_text='0564782193+=-)(%^&*%$#@{}['#映照文字
print(cooperate_text)
book_of_code=''
password_table_1=book_of_code.maketrans(original_text,cooperate_text)#密码本
password_table_2=book_of_code.maketrans(cooperate_text,original_text)#解密本
print(password_table_1,password_table_2)
text=input('请输入需要加密的文字：')
text_1=text.translate(password_table_1)#加密
print('加密的文字为：',text_1,)
text_2=input('请输入需要解密的文字：')
text_3=text_2.translate(password_table_2)#解密
print('解密的文字为',text_3)