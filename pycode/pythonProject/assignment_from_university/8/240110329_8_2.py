a, b = int(input('请输入a的值:')), int(input('请输入b的值(不为零):'))
c = a / b
print(f'{a}/{b}保留一位小数的结果为{str(round(c, 1)).rjust(6,  "=")}',
      f'{a}/{b}保留两位小数的结果为{str(round(c, 2)).rjust(6,  "=")}',
      f'{a}/{b}保留三位小数的结果为{str(round(c, 3)).rjust(6,  "=")}',
      sep='\n')
