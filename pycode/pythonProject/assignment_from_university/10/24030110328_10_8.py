import random
num_global = 0


def count_selected_fruit(first_fruit, second_fruit, *args):
    list_target = ['香蕉', '草莓', '苹果', '梨子', '西瓜', '芒果', '葡萄']
    list_get = [first_fruit, second_fruit] + [i for i in args]
    re_list = []
    re_num = 0
    global num_global
    num_global += 1
    num = 0
    while num < 100:
        re_list.append(random.choice(list_target))
        num += 1
    for item in list_get:
        re_num += re_list.count(item)
    print(f"第{num_global}次共得到了{re_num}个{','.join(list_get)}")


count_selected_fruit('梨子', '芒果')
count_selected_fruit('香蕉', '草莓', '苹果')
count_selected_fruit('苹果', '梨子', '西瓜', '芒果')
count_selected_fruit('草莓', '苹果', '梨子', '西瓜', '芒果')
count_selected_fruit('梨子')
