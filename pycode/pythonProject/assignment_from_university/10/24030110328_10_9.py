import random
num_global = 0


def count_two_fruit(first_fruit, second_fruit, k=100):
    list_target = ['香蕉', '草莓', '苹果', '梨子', '西瓜', '芒果', '葡萄']
    re_list = []
    global num_global
    num_global += 1
    num = 0
    while num < k:
        re_list.append(random.choice(list_target))
        num += 1
    re_num_f, re_num_s = re_list.count(first_fruit), re_list.count(second_fruit)
    print(f"第{num_global}次共得到了{re_num_f}个{first_fruit}，{re_num_s}个{second_fruit}")


count_two_fruit('梨子', '芒果')
count_two_fruit('香蕉', '草莓', 1000)
count_two_fruit(k=200, first_fruit='芒果', second_fruit='草莓')
