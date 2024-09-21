dic = {'gfq': [5, 6, 7, 8], 'beat': [6, 12, 10, 8], 'is': [10, 11, 7, 5], 'for': [1, 2, 5]}
dic_value = {}
for v in dic.values():
    for item in v:
        dic_value[item] = item #将取出的每个数字都放入dic_value，由于同一个数字的key一样，所以重复数字会消去
output=[i for i in dic_value.values()]
output.sort()
print(output)