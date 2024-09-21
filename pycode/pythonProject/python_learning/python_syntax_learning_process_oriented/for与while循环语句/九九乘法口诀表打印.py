for i in range(1,10):#取用乘法口诀表中的第1个因数
    lis=''#设置空字符串以承接得到的乘法口诀表中的公式
    indent=' '#用来给每一次lis的加法增加一个空格
    for j in range(1,10):#取用乘法口诀表中的第2个因数
        if i < j:#判断乘法口诀表中第1个因数小于等于第2个因数，反之就停止循环
            break
        n = i * j
        res=f'{i}x{j}={n}'
        lis = lis + res + indent
        # if i < j:
        #     continue
        # n = i * j
        # res=f'{j}x{i}={n}'
        # lis=lis+res+indent
        #break或者continue都可以
    print(lis)