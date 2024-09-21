for i in range(1,10):#取九行
    if i <= 5:#用来作分类，前面越来越多，后面越来越少
        for j in range(1,i+1):
            print('*',end=' ')#打印一行
        print()#换行符
    else:
        for j in range(1, 11-i):
            print('*', end=' ')
        print()
