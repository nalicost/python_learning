tuple_unit = ('元', '角', '分')
deal = input('请输入一个两位小数：')
deal_li = deal.split('.')
deal_li[1:3] = deal_li[1]
re = ''
for item in range(len(deal_li)):
    if int(deal_li[item]) != 0:
        re += deal_li[item] + tuple_unit[item]
print(re)
