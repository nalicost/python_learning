import random
num_global = 0


def count_apple():
    list_target = ['香蕉', '草莓', '苹果', '梨子', '西瓜', '芒果', '葡萄']
    re_list = []
    num = 0
    global num_global
    num_global += 1
    while num < 100:
        re_list.append(random.choice(list_target))
        num += 1
    print(f"第{num_global}次共得到了{re_list.count('苹果')}个苹果")


count_apple()
count_apple()
count_apple()
