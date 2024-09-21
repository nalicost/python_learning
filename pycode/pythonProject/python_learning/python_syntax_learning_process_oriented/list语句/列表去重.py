a_list=[0, 'abc',1, 3, 4, 5, 6, 7, 8,'abc', 'abc', 1, 4, 8,'df','df', 0, 8, 9, 5, 1, 0, 4, 2, 5, 3, 1, 8, 7, 0, 9, 9, 5, 1, 7, 0, 8, 3, 5, 2, 4, 1, 3, 8, 6]
b_list=[]
# for i in a_list:
#     if i not in b_list:
#         b_list.append(i)
# a_list=b_list
# print(a_list)


#方法2:占用内存小
for i in range(len(a_list)-1, 0, -1):
    if a_list.count(a_list[i])>1:
        a_list.remove(a_list[i])
print(a_list)