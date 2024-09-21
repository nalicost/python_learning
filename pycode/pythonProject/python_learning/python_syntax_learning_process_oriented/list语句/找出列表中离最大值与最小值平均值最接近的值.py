a_list=[86, 65, 25, 77, 92, 69, 53, 90, 98, 17, 76, 40, 10, 56, 77, 17, 98, 81, 68, 21, 49, 94, 30, 12, 92, 32, 63, 72, 20, 77, 5, 24, 6, 19, 25, 94, 78, 17, 88, 37, 34, 19, 13, 62, 24, 92, 98]
j_max=a_list[0]
j_min=a_list[0]
for i in a_list:
    if i > j_max:
        j_max=i
    elif i < j_min:
        j_min=i
average=(j_max+j_min)/2
average_d_min_nul=abs(a_list[0]-average)
average_d_min=a_list[0]
for i in a_list:
    if abs(i-average)<average_d_min_nul:
        average_d_min_nul=abs(i-average)
        average_d_min=i
print(average_d_min)