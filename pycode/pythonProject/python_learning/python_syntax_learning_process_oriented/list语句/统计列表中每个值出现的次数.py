a_list=[0, 1, 2, 3, 4, 5, 6, 7, 8,'abc', 1, 4, 'abc', 8,'df','df', 0, 8, 9, 5, 1, 0, 4, 2, 5, 3, 1, 8, 7, 0, 9, 9, 5, 1, 7, 0, 8, 3, 5, 2,'hg', 1, 3, 8, 6]
b_list=[]
for i in a_list:
    if i not in b_list:
        b_list.append(i)
for j in b_list:
    nul=a_list.count(j)
    print(f'{j}有{nul}个')