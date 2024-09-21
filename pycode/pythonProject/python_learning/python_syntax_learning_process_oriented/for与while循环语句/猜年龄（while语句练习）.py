#本次作业无答案，仅做了修改，会标识出来
i=0#计数器
while i < 3:#判断计数器，确认循环次数
    age=(input('你猜测的年龄是：'))#用户互动
    if age.isdigit():#此段判断为修改内容，记住此语法，判断输入内容是否合法，即是否为数字
        age=int(age)#更改为整型
    else:
        print("不符合要求，重新输")
        continue
    if age == 25:
        print('答对了')
        break#此句为修改内容，注意任务结束后要结束程序
    elif age > 25:
        print('大了')
    elif age < 25:
        print('小了')
    i +=1#此句为修改内容，注意加法可简写如此，要学会使用
    if i == 3:#判断是否继续的条件
        print('笨，有猜错了，你还要继续吗？')
        again=input("yes or no:").upper().strip()#输入关键词
        if again == 'YES':#判断关键词
            i=0#重置变量，使得继续
        else:
            print('byebye')#此句为修改内容，注意任务结束后要结束程序