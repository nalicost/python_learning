height = 100
x = 0
x+=height
for i in range(1,11):
    height = height/2
    x+=height*2
print(f'下落{x}米')
#错误答案示范
# height=100
# distance=0
# count=0
# while count<10:
#     count+=1
#     distance+=height
#     height=height/2
#     distance+=height#错误原因在这里，由于第十次第二次加法在下一次循环，所以少加一个高度
# print(distance)
#思路借鉴：虽然写错了，但是将运动过程分段的思想是可以学习的