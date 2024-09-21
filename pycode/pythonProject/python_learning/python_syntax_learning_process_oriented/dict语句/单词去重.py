#Python is gread and Java is also great
input=input('您输入的字符是 >:')
list_input=input.split(' ') #将输入的英文字符以空格隔开变为list
output_dict={}
for k in list_input:
    output_dict[k]=k #同样的通过同一个数值对应同一个value来去重
print('output:',' '.join(output_dict.values()))