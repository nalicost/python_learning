"""
                        学生管理系统——业务逻辑部分
"""


class StudentManagerController:
    __student_list = []

    @staticmethod
    def add_student(student_info):
        StudentManagerController.__student_list.append(student_info)

    @classmethod
    def student_list(cls):
        return cls.__student_list

    @classmethod
    def del_student(cls, student_id):
        for student in cls.__student_list:
            if student.id == int(student_id):
                cls.__student_list.remove(student)
                return True
        return False

    @classmethod
    def update_student_info(cls, revise_object):
        for student in cls.__student_list:
            if revise_object.id_stu.isdigit():
                if student.id == int(revise_object.id_stu):
                    return cls.revise_student_info(revise_object, student)
                else:
                    print('请输入存在的学生编号')
                    return False
            print('请输入为正整数的学生编号')
            return False

    @classmethod
    def revise_student_info(cls, revise_object, student):
        if revise_object.section_stu == 'name':
            student.name = revise_object.content_stu
            return True
        elif revise_object.section_stu == 'age':
            if revise_object.judge_error():
                student.age = int(revise_object.content_stu)
                return True
        elif revise_object.section_stu == 'score':
            if revise_object.judge_error():
                student.score = int(revise_object.content_stu)
                return True
        else:
            print('操作失败，请输入存在的修改方面')
        return False


class ErrorController:

    @staticmethod
    def judge_error(self):
        try:
            self.judge_def()
        except ValueError:
            self.show_error()
            return False
        else:
            return True

    @staticmethod
    def show_error():
        pass

    def judge_def(self):
        pass


class ChoiceError(ErrorController):
    def __init__(self):
        self.choice = input('你选择的功能是：>:')

    def judge_error(self):
        return super().judge_error(self)

    @staticmethod
    def show_error():
        print('请输入0-5整数')

    def judge_def(self):
        if not self.choice.isdigit() or not 1 <= int(self.choice) <= 5:
            raise ValueError


class InfoError(ErrorController):
    def __init__(self):
        self.name = input('学生姓名是:>')
        self.score = input('学生成绩是:>')
        self.age = input('学生年龄是:>')

    def judge_error(self):
        return super().judge_error(self)

    @staticmethod
    def show_error():
        print('学生成绩与学生年龄请输入正整数,且年龄,成绩在1-100之间')

    def judge_def(self):
        if (not self.age.isdigit() or not self.score.isdigit() or not 1 <= int(self.score) <= 100
                or not 1 <= int(self.age) <= 100):
            raise ValueError


class ReviseInfoError(ErrorController):
    def __init__(self):
        self.id_stu = input('你修改学生信息的编号是:>')
        self.section_stu = input('你修改学生信息的方面是:>')
        self.content_stu = input('你修改学生信息的内容是:>')

    def judge_error(self):
        return super().judge_error(self)

    @staticmethod
    def show_error():
        print('学生成绩与学生年龄请输入正整数,且年龄,成绩在1-100之间')

    def judge_def(self):
        if not self.content_stu.isdigit() or not 1 <= int(self.content_stu) <= 100:
            raise ValueError
