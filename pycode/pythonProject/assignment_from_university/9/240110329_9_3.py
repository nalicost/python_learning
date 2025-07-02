with open(r'C:\Users\zhang\Desktop\东华大学\newscore.txt', 'r', encoding='utf8') as f:
    file_list = f.readlines()
config_range = ([90, 100, '[90, 100]', 0], [80, 90, '[80, 90)', 0],
                [70, 80, '[70,80)', 0], [60, 70, '[60, 70)', 0], [0, 60, '[0, 60)', 0])
for item in file_list:
    obj = int(item.split(',')[-1])
    if obj == 100:
        config_range[0][3] += 1
        continue
    for sub in config_range:
        if sub[0] <= obj < sub[1]:
            sub[3] += 1
for item in config_range:
    print(item[2], '有', item[3], '人', sep='')
