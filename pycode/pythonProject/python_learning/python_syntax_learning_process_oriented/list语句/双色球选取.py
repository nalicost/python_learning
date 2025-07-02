import random
# #第一版：通过多次循环实现多次选取号码，没什么可说的
# i=1
# list_r=[i for i in range(1,34)]
# list_b=[i for i in range(1,17)]
# list_choice=[]
# list_reword=[]
# while i < 7:
#     user_choice_r=input(f'您选择的第{i}个红球号码是：').strip()
#     if user_choice_r.isdigit() and int(user_choice_r) > 0 and int(user_choice_r) < 34 and int(user_choice_r) not in list_choice:
#         list_choice.append(int(user_choice_r))
#         i+=1
#     else:
#         print('请输入符合要求的号码。')
# while i < 8:
#     user_choice_b = input('您选择的蓝球号码是：').strip()
#     if user_choice_b.isdigit() and int(user_choice_b) > 0 and int(user_choice_b) < 17 :
#         list_choice.append(int(user_choice_b))
#         break
#     else:
#         print('请输入符合要求的号码。')
# print(list_choice)
# k=random.sample(list_r,6)
# list_reword+=k
# k=random.sample(list_b,1)
# list_reword+=k
# print('本次的开奖号码为：',list_reword)
# if list_reword==list_choice : print('你中奖了。')
# else: print("还得积积德。")





#第二版修改：通过将上方大量重复的代码中不同的改为变量，一定程度上改变了其扩展性，但若要增加要求，则需重新增加并修改语句
# i=1
# list_choice=[]
# list_reword=[]
# while i < 8:
#     colour,b,k='红',34,i
#     if i==7:
#         colour,b,k='蓝',17,i-6
#     user_choice=input(f'您选择的第{k}个{colour}球号码是：').strip()
#     if user_choice.isdigit() and 0 < int(user_choice) < b and colour+user_choice not in list_choice:
#             choice=colour+user_choice
#             list_choice.append(choice)
#             i+=1
#     else:
#         print('请输入符合要求的号码。')
# print(list_choice)
# for i in range(2):
#     b,k,colour=34,6,'红'
#     if i==1:
#         b,k,colour=17,1,'蓝'
#     x=random.sample(range(1,b),k)
#     list_reword+=[colour+str(i) for i in x]
# print('本次的开奖号码为：',list_reword)
# if list_reword==list_choice : print('你中奖了。')
# else: print("还得积积德。")6





#第三版修改：将所有重复的循坏中不一样的值通过嵌套列表进行赋值，取代由人工写的条件语句，极大的增加了其可扩展性，只需增加列表中的值即可实现相似的功能

list_choice_r=[]
list_choice_b=[]
list_reward_r=[]
list_reward_b=[]
list_reward=[[[6,1],1],[[6,0],2],[[5,1],3],[[5,0],4],[[4,1],4],[[4,0],5],[[3,1],5],[[2,1],6],[[1,1],6],[[0,1],6]]#奖励列表，将各种情况的奖励要求及等级写入其中
list_same=[]
list_acquirement=[[6,'红',33,list_choice_r,list_reward_r,0],[1,'蓝',16,list_choice_b,list_reward_b,1]]#将抽取的规则，颜色，数量，包括得出的结果需放入的列表写入其中
for acquirement in list_acquirement:#循环要求列表，以便下方进行取值
    count=0
    while count < acquirement[0]:
        choice=input(f'请选择第{count+1}个{acquirement[1]}球：')
        if choice.isdigit() and 0 < int(choice) <= acquirement[2] and int(choice) not in acquirement[3]:#判断语句是否合法
            acquirement[3].append(int(choice))
            count+=1
        else:
            print('请输入正确的值。')
    b=random.sample(range(1,acquirement[2]+1),acquirement[0])
    for k in b:
        acquirement[4].append(k)
    same=0
    for i in acquirement[3]:
        if i in acquirement[4]:
            same+=1
    list_same.append(same)
print('你的选择是：',list_choice_r,list_choice_b)
print('本次开奖的号码是：',list_reward_r,list_reward_b)
for j in list_reward:#类似的，通过循环奖励列表，确定获奖情况
    if j[0]==list_same:
        print(f'你获得了{j[1]}等奖')
        break
else:print('还得积积德。')