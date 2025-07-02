"""
                面向对象的思路完成学生成绩录入与输出
"""


class Student:
    def __init__(self, name, score, gender):
        """
                学生类的数据成员
        :param name: 名字
        :param score: 成绩
        :param gender: 性别
        """
        self.name = name
        self.score = score
        self.gender = gender

    def print_score(self):
        """
                个人信息打印
        """
        print(f'姓名：{self.name}, 性别：{self.gender}， 成绩： {self.score}')


def student_object(output_list):
    """
            学生信息录入
    :param output_list: 输出列表
    :return: 如果学生姓名为空，返回0
    """
    name = input('姓名:>')
    if name:
        score = input('成绩:>')
        gender = input('性别:>')
        student_information = Student(name, score, gender)
        output_list.append(student_information)
    else:
        return 0


def student_information_output(target_list):
    """
            学生信息打印
    :param target_list: 目标列表
    """
    for student in target_list:
        student.print_score()
    target_list[1].print_score()


# i = None
# student_information_list = []
# while i != 0:
#     i = student_object(student_information_list)
# student_information_output(student_information_list)
#
# list_01 = [Student('aa', 30, '男'), Student('ab', 100, '女'), Student('ac', 200, '女')]


def search_01(target_list, search_object):
    """
            依据姓名搜查对象
    :param target_list: 目标列表
    :param search_object: 寻找对象
    """
    for student in target_list:
        if student.name == search_object:
            print(student.name, student.score)
            break
    else:
        print('没找到')


def search_02(target_list, search_object):
    """
            依据性别搜查对象
    :param target_list: 目标列表
    :param search_object: 搜索对象
    """
    for student in target_list:
        if student.gender == search_object:
            print(student.name, student.score)


def conclude_score(target_list):
    """
            统计分数大于30
    :param target_list: 查找列表
    :return: 返回统计数量
    """
    num = 0
    for student in target_list:
        if student.score >= 30:
            num += 1
    return num


def return_0(target_list):
    """
            统一修改成绩
    :param target_list: 修改对象
    """
    for student in target_list:
        student.score = 0


def print_name(target_list):
    """
            打印学生姓名
    :param target_list: 打印列表
    """
    for student in target_list:
        print(student.name)


def max_score(target_list):
    """
            返回成绩最大的对象
    :param target_list: 目标列表
    :return: 成绩最大的对象
    """
    max_score = target_list[0]
    for student in target_list:
        if student.score > max_score.score:
            max_score = student
    return max_score


search_01(list_01, 'aa')
search_02(list_01, '女')
print(conclude_score(list_01))
print(max_score(list_01).name)
print('-----------')
return_0(list_01)
print(list_01[0].score, list_01[1].score)
print_name(list_01)
