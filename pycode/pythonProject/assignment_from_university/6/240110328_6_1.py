score = input("请输入五位同学的成绩，中间以英文逗号分割:")
score = score.replace("，", ",")
score_list = score.split(",")
score_list = sorted(score_list, reverse=True)
score_sum = 0
print('从高分到低分输出成绩:', end='')
for score_str in score_list:
    print(score_str, end=',')
    score_sum += int(score_str)
score_avg = score_sum / 5
print("平均成绩为:{:.1f}".format(score_avg))
