#整个程序可以正常完成字数统计，唯一遗憾的是，由于无法直接输入长字符，必须一段段输入，其次统计可更详细，望以后学完自定义函数来进行优化修改
amount_all=0#下方五行用来输出统计结果
amount_str=0
amount_nul=0
amount_spec=0
amount_space=0
paragraph=1#用来标识输入段落
article=''
while True:
    prt=input(f'请输入第{paragraph}文字：')
    paragraph+=1
    article+=prt
    if not prt:break#此句等价于if len（prt）==0：
for i in article:
    amount_all+=1
    if i.isalpha():
        amount_str+=1
    elif i.isdigit():
        amount_nul+=1
    elif i.isprintable() and not i.isdigit() and not i.isspace() and not i.isalpha():
        amount_spec+=1
    elif i.isspace():
        amount_space+=1
print('总共字数：{amount_all}，数字字数：{amount_nul}，特殊字符字数：{amount_spec}，空格数：{amount_space}，字符字数：{amount_str}'.format(amount_all=amount_all,amount_nul=amount_nul ,amount_spec =amount_spec ,amount_space =amount_space ,amount_str =amount_str))