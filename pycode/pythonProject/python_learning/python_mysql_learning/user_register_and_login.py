"""
                    用户注册登录模拟
"""
import pymysql


class UserLoginView:
    def __init__(self):
        self.server_list = ['退出', '注册', '登录']
        self.server_dict = {0: self.__quit, 1: self.__register, 2: self.__login}
        self.user_login_controller = UserLoginController()

    @staticmethod
    def __return_msg(list_msg):
        if list_msg[0]:
            print(f'{list_msg[1]}成功')
        else:
            print(f'{list_msg[1]}失败，原因：{list_msg[2]}')

    @staticmethod
    def __get_user_and_password(flags=0):
        while True:
            user_name, user_password = input('你的用户名是>:'), input('你的密码是>:')
            if flags:
                password_again = input('确认密码>:')
                if password_again != user_password:
                    print('密码不一致')
                    continue
            return user_name, user_password

    def __display(self):
        print('主菜单'.center(50, '='))
        for i in range(len(self.server_list)):
            print(i, f': {self.server_list[i]}')
        print('结束'.center(50, '='))

    def __choice_server(self):
        try:
            choice = input('你选择的服务是>:')
        except Exception as e:
            print(e)
            return
        self.server_dict[int(choice)]()

    def __register(self):
        result = self.user_login_controller.register(self.__get_user_and_password(1))
        self.__return_msg(result)

    def __login(self):
        result = self.user_login_controller.login(self.__get_user_and_password())
        self.__return_msg(result)

    @staticmethod
    def __quit():
        print('Bye')
        raise StopIteration

    def main(self):
        while True:
            try:
                self.__display()
                self.__choice_server()
            except StopIteration:
                break
            except KeyError:
                print('请输入存在的服务')
            except Exception as e:
                print(e)


class UserLoginController:
    def __init__(self):
        self.user_login_model = UserLoginModel()

    def register(self, user_info):
        try:
            sql_write = r"insert into user values (%s,%s)"
            self.user_login_model.cur.execute(sql_write, user_info)
            self.user_login_model.db.commit()
        except Exception as e:
            self.user_login_model.db.rollback()
            return 0, '注册', e
        return 1, '注册'

    def login(self, user_info):
        sql_write = r"select password from user where name='%s'" % user_info[0]
        self.user_login_model.cur.execute(sql_write)
        result = self.user_login_model.cur.fetchone()
        if not result:
            return 0, '登录', '用户不存在'
        else:
            if result[0] == user_info[1]:
                return 1, '登录'
            else:
                return 0, '登录', '密码错误'


class UserLoginModel:
    def __init__(self):
        self.db = pymysql.connect(host='localhost',
                                  port=3306,
                                  user='root',
                                  password='Zjy20170132',
                                  charset='utf8',
                                  database='software_a')
        self.cur = self.db.cursor()


if __name__ == '__main__':
    server = UserLoginView()
    server.main()
