import random
num_global = 0


def count_one_fruit(fruit_name):
    list_target = ['香蕉', '草莓', '苹果', '梨子', '西瓜', '芒果', '葡萄']
    re_list = []
    num = 0
    global num_global
    num_global += 1
    while num < 100:
        re_list.append(random.choice(list_target))
        num += 1
    print(f"第{num_global}次共得到了{re_list.count(fruit_name)}个{fruit_name}")
    num_global = 0


count_one_fruit('香蕉')
count_one_fruit('草莓')
count_one_fruit('苹果')
