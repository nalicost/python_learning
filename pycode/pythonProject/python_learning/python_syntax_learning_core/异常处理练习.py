"""
            关于异常处理
"""
# 练习一：学生成绩录入，满足为整数，且值在0-100之间


def get_stu_score():
    while True:
        try:
            student_score = int(input('学生的成绩是:>'))
            if not 0 <= student_score <= 100: raise ValueError
        except ValueError:
            print('请输入整数且整数范围在0-100之间')
        else:
            student_name = input('学生的姓名是:>')
            return student_name, student_score


print(get_stu_score())
