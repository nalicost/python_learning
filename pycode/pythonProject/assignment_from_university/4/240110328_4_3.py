year_index = int(input('请输入年份值>:'))
if not year_index % 4 and year_index % 100 or not year_index % 400:
    print('是闰年')
else:
    print('不是闰年')
