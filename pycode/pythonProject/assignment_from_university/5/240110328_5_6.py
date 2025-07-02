num_change_row = 0
for i in range(2, 1000):
    if num_change_row == 10:
        num_change_row = 0
        print()
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i, end='\t')
        num_change_row += 1
