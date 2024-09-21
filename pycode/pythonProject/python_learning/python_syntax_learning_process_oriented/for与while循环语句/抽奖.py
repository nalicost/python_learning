import random#引入随机函数这一库
i=0
list=[]
for k in range(300):
    list.append(k)
reward=[]
# list=range(300)#注意list为range类型而非列表类型
for n in range(3):
    if n==0:
        i=30
    elif n==1:
        i=6
    elif n==2:
        i=3
    reward=random.sample(list,i)#随机函数在list中抽取的用法
    # list=[i for i in list if i not in reward]#如果使用list=range（300），则需靠此将range类型的list重新生成符合条件的列表
    for j in reward:
        list.remove(j)
    print(reward)