with open(r'C:\Users\zhang\Desktop\东华大学\newscore.txt', 'r', encoding='utf8') as f:
    file_list = f.readlines()
    specialize_dict = {key.split(',')[2]: 0 for key in file_list}
    for item in file_list:
        specialize_dict[item.split(',')[2]] += 1
for key, value in specialize_dict.items():
    print(key, '有', value, '人', sep='')
