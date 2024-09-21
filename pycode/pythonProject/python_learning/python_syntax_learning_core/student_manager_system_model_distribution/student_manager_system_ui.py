"""
                学生管理系统——界面视图部分
"""
from student_manager_system_modell import *


class StudentManagerView:
    __student_manager_controller = StudentManagerController()

    @staticmethod
    def main():
        n = 1
        while n != 0:
            StudentManagerView.__display_student_info()
            n = StudentManagerView.__select_menu()

    @staticmethod
    def __select_menu():
        choice = ChoiceError()
        if choice.judge_error():
            if choice.choice == '1':
                StudentManagerView.__create_student()
            elif choice.choice == '2':
                StudentManagerView.__show_student_info()
            elif choice.choice == '3':
                StudentManagerView.__revise_student_info()
            elif choice.choice == '4':
                StudentManagerView.__del_student_info()
            elif choice.choice == '5':
                StudentManagerView.__sort_student_score_show()
            return int(choice.choice)

    @staticmethod
    def __display_student_info():
        print('0)退出')
        print('1)新建学生信息')
        print('2)查看学生信息')
        print('3)修改学生信息')
        print('4)删除学生信息')
        print('5)成绩降序查看学生信息')

    @staticmethod
    def __create_student():
        while True:
            stu_info = InfoError()
            if stu_info.judge_error():
                StudentModel(stu_info.name, stu_info.score, stu_info.age)
                print('操作成功')
                break

    @staticmethod
    def __show_student_info():
        for student in StudentManagerView.__student_manager_controller.student_list():
            print(student.id, student.name, student.score, student.age)

    @staticmethod
    def __revise_student_info():
        if StudentManagerController.student_list():
            while True:
                revise_info = ReviseInfoError()
                if StudentManagerView.__student_manager_controller.update_student_info(revise_info):
                    print('操作成功')
                    break
        else:
            print('无学生')

    @staticmethod
    def __del_student_info():
        if StudentManagerController.student_list():
            while True:
                id_stu = input('你删除的学生id是:>')
                if id_stu.isdigit():
                    break
                print('请输入存在且为正整数的id')
            print('操作成功')
            return StudentManagerController.del_student(id_stu)
        else: 
            print('无学生')

    @staticmethod
    def __sort_student_score_show():
        list_backup = StudentManagerController.student_list()[::]
        list_backup.sort(key=lambda student01: student01.score, reverse=True)
        for student in list_backup:
            print(student.id, student.name, student.score, student.age)

