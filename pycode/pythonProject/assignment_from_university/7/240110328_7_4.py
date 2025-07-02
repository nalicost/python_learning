factor = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
last_dict = {0: '1', 1: '0', 2: 'X', 3: '9', 4: '8', 5: '7', 6: '6', 7: '5', 8: '4', 9: '3', 10: '2'}
ID = input('请输入18位身份证号>:')
re = 0
for i in range(17):
    re += int(ID[i]) * factor[i]
if last_dict[re % 11] != ID[-1]:
    print('身份证号非法')
else:
    print('身份证号通过验证')
