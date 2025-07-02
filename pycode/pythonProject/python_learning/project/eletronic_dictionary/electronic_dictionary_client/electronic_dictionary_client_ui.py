# -*- encoding:gbk -*-
"""
                本模块为电子词典客户端的ui模块包含ui展示与和bll以及model模块的联动
"""
from electronic_dictionary_client_bll import *


class ElectronicDictionaryUI:
    """
                电子词典ui类
    """
    def __init__(self):
        """
                初始化实例变量
        """
        # 组合复用menu模型
        self.__menu = MenuModel(0, 3)
        # 组合复用传输协议逻辑
        self.__communication_agreement_controller = CommunicationAgreementController()
        # 初始化加载菜单
        self.__get_menu_config()
        # 封装服务方法
        self.__service_dict = {1: self.__login, 2: self.__register, 3: self.__exit,
                               4: self.__seek_word, 5: self.__show_history, 6: self.__quit}

    def __get_menu_config(self):
        """
                菜单加载器
        """
        # 获取配置文件内容
        with open(r'C:\Users\zhang\PycharmProjects\pythonProject\python_learning'
                  r'\project\eletronic_dictionary\electronic_dictionary_client\menu_config.txt') as f:
            line_list = f.readlines()
            # 写入menu中，即层序生成节点
            self.__menu.add_node_order_by_layer(line_list)

    def __show_menu(self):
        """
                展示菜单
        """
        # 显示层数
        print(f'你处于{self.__menu.layer}级界面'.center(50, '='))
        # 遍历获取菜单内容
        for i in range(1, 4):
            # 将元组中菜单汉字获取
            item_show = eval(self.__menu.now_node.degree[i].node)[0]
            # 判断是否为空
            if item_show:
                print(item_show)

    def __choice_service(self):
        """
                服务选择
        """
        choice_ = int(input('你想要选择的服务是>:'))
        # 通过选择，调用对应函数
        self.__service_dict[eval(self.__menu.select_path(choice_))[1]]()

    @staticmethod
    def __input_and_get_re(func, *args):
        """
                    获取输入，并返回处理结果
        :param func:处理输入内容的函数
        :param args:函数的位置参数
        """
        # 循环位置参数列表
        for item in args:
            # 获取位置参数
            item[0] = input(f'{item[1]}>:')
            # 防止空格在用户名内
            if ' ' in item[0]:
                return False, f'{item[1]}不允许有空格'
            # 是否确认
            if item[2]:
                item_confirm = input(f'确认你的{item[1]}>:')
                if item_confirm != item[0]:
                    return False, f'{item[1]}两次不一致'
        # 将位置参数取出
        args = list(map(lambda i: i[0], args))
        return func(*args)

    @staticmethod
    def __repeat_operation(func, *args):
        """
                重复方法器
        :param func:需要重复执行的函数
        :param args:函数需要传入的参数
        """
        while True:
            re, msg = func(*args)
            # 判断是否成功执行函数
            if re:
                return msg
            print(msg.center(50, '='))

    def __login(self):
        """
                    登录方法
        """
        # 通过重复执行获取输入来通过传输协议逻辑类向服务端发送请求来获取处理结果
        msg = ElectronicDictionaryUI.__repeat_operation(self.__input_and_get_re,
                                                        self.__communication_agreement_controller.login,
                                                        [None, '用户名', 0], [None, '密码', 0])
        print(msg.center(50, '='))

    def __register(self):
        """
                            注册方法
        """
        # 通过重复执行获取输入来通过传输协议逻辑类向服务端发送请求来获取处理结果
        msg = ElectronicDictionaryUI.__repeat_operation(self.__input_and_get_re,
                                                        self.__communication_agreement_controller.register,
                                                        [None, '用户名', 0], [None, '密码', 1])
        print(msg.center(50, '='))
        # 返回一层
        self.__menu.select_path()

    def __exit(self):
        """
                            退出方法
        """
        print('Bye')
        self.__communication_agreement_controller.exit()

    def __seek_word(self):
        """
                            查找单词方法
        """
        # 通过重复执行获取输入来通过传输协议逻辑类向服务端发送请求来获取处理结果
        msg = ElectronicDictionaryUI.__repeat_operation(self.__input_and_get_re,
                                                        self.__communication_agreement_controller.seek_word,
                                                        [None, '单词', 0])
        print(msg)
        # 退回上一层
        self.__menu.select_path()

    def __show_history(self):
        """
                            注册方法
        """
        # 通过重复执行获取输入来通过传输协议逻辑类向服务端发送请求来获取处理结果，tuple吧包含返回结果数，和具体结果内容，re为执行是否成功
        re, tuple_ = self.__input_and_get_re(self.__communication_agreement_controller.show_history,
                                             [None, '是否只查看前十条记录(T OR F)', 0])
        # 答应获取内容标题
        print(f'你的{tuple_[1]}条历史记录是'.center(50, '='))
        print(tuple_[0])
        # 退回上一层
        self.__menu.select_path()

    def __quit(self):
        """
                            注销用户方法
        """
        # 打印退出信息
        print('你已退出登录'.center(50, '='))
        self.__communication_agreement_controller.quit()
        # 要退两次，由于要返回第一层，此时在第三层
        self.__menu.select_path()
        self.__menu.select_path()

    def main(self):
        """
                主函数
        """
        # 连接服务端
        self.__communication_agreement_controller.inet_connect()
        # 重复发送请求
        while True:
            try:
                self.__show_menu()
                self.__choice_service()
            # 退出客户端
            except KeyboardInterrupt:
                break
            # 错误处理
            except IndexError:
                print('请输入正确的服务序号')
            # 错误处理
            except ValueError:
                print('请输入正确的服务序号')


if __name__ == '__main__':
    test_ui = ElectronicDictionaryUI()
    test_ui.main()
