import random
result_dict = {}
result_list = []
fruit_tuple = ('香蕉', '草莓', '苹果', '梨子', '西瓜', '芒果', '葡萄')
for i in range(100):
    result_list.append(random.sample(fruit_tuple, 1)[0])
for i in result_list:
    if i not in result_dict:
        result_dict[i] = 1
    else:
        result_dict[i] += 1
for key, value in result_dict.items():
    print(f"{key}出现了{value}次")
