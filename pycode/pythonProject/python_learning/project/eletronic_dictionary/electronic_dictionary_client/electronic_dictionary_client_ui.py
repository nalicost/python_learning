# -*- encoding:gbk -*-
"""
                ��ģ��Ϊ���Ӵʵ�ͻ��˵�uiģ�����uiչʾ���bll�Լ�modelģ�������
"""
from electronic_dictionary_client_bll import *


class ElectronicDictionaryUI:
    """
                ���Ӵʵ�ui��
    """
    def __init__(self):
        """
                ��ʼ��ʵ������
        """
        # ��ϸ���menuģ��
        self.__menu = MenuModel(0, 3)
        # ��ϸ��ô���Э���߼�
        self.__communication_agreement_controller = CommunicationAgreementController()
        # ��ʼ�����ز˵�
        self.__get_menu_config()
        # ��װ���񷽷�
        self.__service_dict = {1: self.__login, 2: self.__register, 3: self.__exit,
                               4: self.__seek_word, 5: self.__show_history, 6: self.__quit}

    def __get_menu_config(self):
        """
                �˵�������
        """
        # ��ȡ�����ļ�����
        with open(r'C:\Users\zhang\PycharmProjects\pythonProject\python_learning'
                  r'\project\eletronic_dictionary\electronic_dictionary_client\menu_config.txt') as f:
            line_list = f.readlines()
            # д��menu�У����������ɽڵ�
            self.__menu.add_node_order_by_layer(line_list)

    def __show_menu(self):
        """
                չʾ�˵�
        """
        # ��ʾ����
        print(f'�㴦��{self.__menu.layer}������'.center(50, '='))
        # ������ȡ�˵�����
        for i in range(1, 4):
            # ��Ԫ���в˵����ֻ�ȡ
            item_show = eval(self.__menu.now_node.degree[i].node)[0]
            # �ж��Ƿ�Ϊ��
            if item_show:
                print(item_show)

    def __choice_service(self):
        """
                ����ѡ��
        """
        choice_ = int(input('����Ҫѡ��ķ�����>:'))
        # ͨ��ѡ�񣬵��ö�Ӧ����
        self.__service_dict[eval(self.__menu.select_path(choice_))[1]]()

    @staticmethod
    def __input_and_get_re(func, *args):
        """
                    ��ȡ���룬�����ش�����
        :param func:�����������ݵĺ���
        :param args:������λ�ò���
        """
        # ѭ��λ�ò����б�
        for item in args:
            # ��ȡλ�ò���
            item[0] = input(f'{item[1]}>:')
            # ��ֹ�ո����û�����
            if ' ' in item[0]:
                return False, f'{item[1]}�������пո�'
            # �Ƿ�ȷ��
            if item[2]:
                item_confirm = input(f'ȷ�����{item[1]}>:')
                if item_confirm != item[0]:
                    return False, f'{item[1]}���β�һ��'
        # ��λ�ò���ȡ��
        args = list(map(lambda i: i[0], args))
        return func(*args)

    @staticmethod
    def __repeat_operation(func, *args):
        """
                �ظ�������
        :param func:��Ҫ�ظ�ִ�еĺ���
        :param args:������Ҫ����Ĳ���
        """
        while True:
            re, msg = func(*args)
            # �ж��Ƿ�ɹ�ִ�к���
            if re:
                return msg
            print(msg.center(50, '='))

    def __login(self):
        """
                    ��¼����
        """
        # ͨ���ظ�ִ�л�ȡ������ͨ������Э���߼��������˷�����������ȡ������
        msg = ElectronicDictionaryUI.__repeat_operation(self.__input_and_get_re,
                                                        self.__communication_agreement_controller.login,
                                                        [None, '�û���', 0], [None, '����', 0])
        print(msg.center(50, '='))

    def __register(self):
        """
                            ע�᷽��
        """
        # ͨ���ظ�ִ�л�ȡ������ͨ������Э���߼��������˷�����������ȡ������
        msg = ElectronicDictionaryUI.__repeat_operation(self.__input_and_get_re,
                                                        self.__communication_agreement_controller.register,
                                                        [None, '�û���', 0], [None, '����', 1])
        print(msg.center(50, '='))
        # ����һ��
        self.__menu.select_path()

    def __exit(self):
        """
                            �˳�����
        """
        print('Bye')
        self.__communication_agreement_controller.exit()

    def __seek_word(self):
        """
                            ���ҵ��ʷ���
        """
        # ͨ���ظ�ִ�л�ȡ������ͨ������Э���߼��������˷�����������ȡ������
        msg = ElectronicDictionaryUI.__repeat_operation(self.__input_and_get_re,
                                                        self.__communication_agreement_controller.seek_word,
                                                        [None, '����', 0])
        print(msg)
        # �˻���һ��
        self.__menu.select_path()

    def __show_history(self):
        """
                            ע�᷽��
        """
        # ͨ���ظ�ִ�л�ȡ������ͨ������Э���߼��������˷�����������ȡ��������tuple�ɰ������ؽ�������;��������ݣ�reΪִ���Ƿ�ɹ�
        re, tuple_ = self.__input_and_get_re(self.__communication_agreement_controller.show_history,
                                             [None, '�Ƿ�ֻ�鿴ǰʮ����¼(T OR F)', 0])
        # ��Ӧ��ȡ���ݱ���
        print(f'���{tuple_[1]}����ʷ��¼��'.center(50, '='))
        print(tuple_[0])
        # �˻���һ��
        self.__menu.select_path()

    def __quit(self):
        """
                            ע���û�����
        """
        # ��ӡ�˳���Ϣ
        print('�����˳���¼'.center(50, '='))
        self.__communication_agreement_controller.quit()
        # Ҫ�����Σ�����Ҫ���ص�һ�㣬��ʱ�ڵ�����
        self.__menu.select_path()
        self.__menu.select_path()

    def main(self):
        """
                ������
        """
        # ���ӷ����
        self.__communication_agreement_controller.inet_connect()
        # �ظ���������
        while True:
            try:
                self.__show_menu()
                self.__choice_service()
            # �˳��ͻ���
            except KeyboardInterrupt:
                break
            # ������
            except IndexError:
                print('��������ȷ�ķ������')
            # ������
            except ValueError:
                print('��������ȷ�ķ������')


if __name__ == '__main__':
    test_ui = ElectronicDictionaryUI()
    test_ui.main()
