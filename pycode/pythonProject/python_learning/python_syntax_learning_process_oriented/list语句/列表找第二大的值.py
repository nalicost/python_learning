import copy
a_list=[86, 65, 25, 77, 92, 69, 53, 90, 98, 17, 76, 40, 10, 56, 77, 17, 98, 81, 68, 21, 49, 94, 30, 12, 92, 32, 63, 72, 20, 77, 5, 24, 6, 19, 25, 94, 78, 17, 88, 37, 34, 19, 13, 62, 24, 92, 98]
b_list=[]




#方法1：直接用内部就有的sort函数，先去重再排序
# for i in a_list:
#     if i not in b_list:
#         b_list.append(i)
# b_list.sort(reverse=True)
# print(b_list[1])

#方法2：通过找两次最大值，每次将最大值删去，计算量较小
# b_list=copy.deepcopy(a_list)
# for i in range(2):
#     j = b_list[0]
#     for i in b_list:
#         if i > j:
#             j=i
#     nul=b_list.count(j)
#     for i in range(nul):
#         b_list.remove(j)
# print(j)

#通过比较有几个数比取出的数大，将符合数量的数取出，相对计算量大
# for i in a_list:
#     if i not in b_list:
#          b_list.append(i)
# for i in b_list:
#     k=0
#     for j in b_list:
#         if i < j:
#             k+=1
#     if k==1:
#         print(i)
#         break

#冒泡排序：通过比较前后两个数大小，若后比前小，交换位置，使得最大值次大值.....依次排列在最右处，计算量最小
for i in a_list:
    if i not in b_list:
        b_list.append(i)
a_list=b_list
for i in range(2):
    for j in range(len(a_list)-1):
        if a_list[j] > a_list[j+1]:
            k=a_list[j]
            a_list[j]=a_list[j+1]
            a_list[j+1]=k
    j=a_list[-1]
    a_list.remove(a_list[-1])
print(j)