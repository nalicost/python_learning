with open(r'C:\Users\zhang\Desktop\东华大学\newscore.txt', 'r', encoding='utf8') as f:
    file_list = f.readlines()
dict_deal = {}
for item in file_list:
    obj = item.split(',')[0][0:2]
    if obj not in dict_deal:
        dict_deal[obj] = 1
    else:
        dict_deal[obj] += 1
for key, value in dict_deal.items():
    print(key, '有', value, '人', sep='')
