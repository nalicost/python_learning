a_list=[86, 65, 25, 77, 92, 69, 53, 90, 98, 17, 76, 40, 10, 56, 77, 17, 98, 81, 68, 21, 49, 94, 30, 12, 92, 32, 63, 72, 20, 77, 5, 24, 6, 19, 25, 94, 78, 17, 88, 37, 34, 19, 13, 62, 24, 92, 98]
b_list=[65, 25, 77, 92, 69, 53, 90, 98, 17, 76, 40, 10, 56, 77, 17, 98, 81]
c_list=[0, 1, 2, 3, 4, 5, 6, 7, 8,'abc', 1, 4, 'abc', 8,'df','df', 0, 8, 9, 5, 1, 0, 4, 2, 5,]
for i in b_list:
    if i not in a_list:
        print(False)
        break
else:
    print(True)
for i in c_list:
    if i not in a_list:
        print(False)
        break
else:
    print(True)