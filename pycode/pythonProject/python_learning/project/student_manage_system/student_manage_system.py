"""
        学生管理系统
        项目计划：1、完成数据模型类
                2、创建逻辑控制类
                3、完成私有数据__student_list
                4、行为：获取列表
                5、行为：添加学生
"""


class StudentManagerController:
    __student_list = []

    @staticmethod
    def __add_student(student_info):
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
    def update_student_info(cls, student_id, section, content):
        for student in cls.__student_list:
            if student.id == int(student_id):
                if section == 'name':
                    student.name = content
                elif section == 'age':
                    student.age = int(content)
                elif section == 'score':
                    student.score = float(content)
                else:
                    return False
                return True
        return False


class StudentModel:
    id_num = 0
    stu_manage = StudentManagerController()

    def __init__(self, name, score, age):
        StudentModel.id_num += 1
        self.name = name
        self.score = float(score)
        self.age = int(age)
        self.id = StudentModel.id_num
        StudentModel.stu_manage._StudentManagerController__add_student(self)

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


class StudentManagerView:
    __student_manager_controller = StudentManagerController()

    @staticmethod
    def main():
        n = 1
        while n != 0:
            StudentManagerView.__display_student_info()
            n = int(StudentManagerView.__select_menu())

    @staticmethod
    def __select_menu():
        choice = input('你选择的功能是：>:')
        if choice == '1':
            StudentManagerView.__create_student()
        elif choice == '2':
            StudentManagerView.__show_student_info()
        elif choice == '3':
            if StudentManagerView.__revise_student_info():
                print('操作成功')
            else:
                print('操作失败')
        elif choice == '4':
            if StudentManagerView.__del_student_info():
                print('操作成功')
            else:
                print('操作失败')
        elif choice == '5':
            StudentManagerView.__sort_student_score_show()
        return choice

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
        name = input('学生姓名是:>')
        score = input('学生成绩是:>')
        age = input('学生年龄是:>')
        StudentModel(name, score, age)

    @staticmethod
    def __show_student_info():
        for student in StudentManagerView.__student_manager_controller.student_list():
            print(student.id, student.name, student.score, student.age)

    @staticmethod
    def __revise_student_info():
        id_stu = input('你修改学生信息的编号是:>')
        section_stu = input('你修改学生信息的方面是:>')
        content_stu = input('你修改学生信息的内容是:>')
        return StudentManagerView.__student_manager_controller.update_student_info(id_stu, section_stu, content_stu)

    @staticmethod
    def __del_student_info():
        id_stu = input('你删除的学生id是:>')
        return StudentManagerController.del_student(id_stu)

    @staticmethod
    def __sort_student_score_show():
        list_backup = StudentManagerController.student_list()[::]
        list_backup.sort(key=lambda student: student.score, reverse=True)
        for student in list_backup:
            print(student.id, student.name, student.score, student.age)


    # 参考代码，提示，不必死板，传进来的内容可以是打包好的整体,不修改的可使用默认参数不传参

    """
    def update_student_info(cls, str_info):
        for student in cls.__student_list:
            if student.id == str_info.id:
                student.name = str_info.name
                student.age = str_info.age
                student.score = str_info.score
                return True
        return False
    """


# 参考答案:添加需要外部调取，其他一致,由于只有一个对象故不需传东西


"""
class StudentManagerController:
    def __init__(self):
        self.__student_list = []

    def add_student(self, student_info):
        self.__student_list.append(student_info)

    def student_list(self):
        return self.__student_list
"""

StudentManagerView.main()