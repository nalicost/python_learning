import random
f=open('双色球.txt','a')
i = 1
while i != 0:
    requirement = [[34, 6, [],[]], [17, 1, [],[]]]#用来循环，满足需求可以使下方原本重复的代码中的关键词可以更换为变量，减少重复代码
    for item in requirement:
        for k in range(1,item[0]):#生成有指定数量空格的list
            t = '  '
            item[2].append(t)
        item[3]=random.sample(range(1,item[0]),item[1])#随机函数取指定范围指定数量的数字
        for j in item[3]:
            item[2][j-1] = f'{j}'.zfill(2)#将取到的数字替换相应位置的空格，达到每个数字间的空格一致，同时将所有字符的长度补充为两格
        output=' '.join(item[2])#将列表转化为字符串
        f.write(f'{output}-----')
    f.write('\n')
    h=input(':>')#保证代码不会无限制继续导致出错