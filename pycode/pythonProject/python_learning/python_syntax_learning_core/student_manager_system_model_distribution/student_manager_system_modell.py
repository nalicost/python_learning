"""
                学生管理系统——数据模型部分
"""
from student_manager_system_bll import *


class StudentModel:
    id_num = 0
    stu_manage = StudentManagerController()

    def __init__(self, name, score, age):
        StudentModel.id_num += 1
        self.name = name
        self.score = int(score)
        self.age = int(age)
        self.id = StudentModel.id_num
        StudentModel.stu_manage.add_student(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value
