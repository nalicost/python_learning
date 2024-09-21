# for i in range(10):
#     if i%2 == 0:
#         print("女",i)
#     else:
#         print("男",i)











#判断法来使程序在四层后退出程序
# for floor in range(1,7):#用来循环取楼层
#     if floor == 3:#判断特殊楼层
#         print(f'你当前在第{floor}层'.center(50, '-'))
#         print("此层不通")
#         continue#跳过此次循环（为第一个for）
#     elif floor ==5:#判断特殊楼层
#         break#终止本次循环（为第一个for）
#     print(f'你当前在第{floor}层'.center(50,'-'))
#     for room in range(1,10):#用来循环取房间号
#         if floor == 4 and room == 4:#判断特殊楼层的特殊房间
#             print("oh，my god")
#             break#终止本次循环（为第二个for）
#         else:
#             print(f'你在{floor}0{room}室')



#标识位法来退出程序
nul=[]#这个是标识物，同时此标志物无需每次更新放外面
for floor in range(1,7):#用来循环取楼层
    if floor == 3:#判断特殊楼层
        print(f'你当前在第{floor}层'.center(50, '-'))
        print("此层不通")
        continue#跳过此次循环（为第一个for）
    elif '0' in nul:#这个是标识位，判断标识是否改变
        break
    print(f'你当前在第{floor}层'.center(50,'-'))
    for room in range(1,10):#用来循环取房间号
        if floor == 4 and room == 4:#判断特殊楼层的特殊房间
            print("oh，my god")
            nul.append("0")#满足条件更改标识物
            break#终止本次循环（为第二个for）
        else:
            print(f'你在{floor}0{room}室')