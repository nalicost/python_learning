# -*- encoding:gbk -*-
"""
            ��ģ��Ϊ���Ӵʵ�ͻ��˵�ҵ���߼�ģ�����������Ӧ�Ĵ�����ui��modelģ�������
"""
from electronic_dictionary_client_model import *
import socket
# ����˵�ַ
ADDR = ('127.0.0.1', 10090)


class CommunicationAgreementController:
    """
                ����Э���߼���
    """
    def __init__(self):
        """
                ��ʼ��ʵ������
        """
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def inet_connect(self):
        """
                ������������
        """
        self.__socket.connect(ADDR)

    def __handle_rp(self):
        """
                ������Ӧ
        """
        # ���շ������Ӧ
        data = self.__socket.recv(1024).decode('gbk')
        # ����Э��
        rp_ = eval(data)
        # ������Э������
        return rp_.content_type == 'T', rp_.content

    def __send_rq(self, rq_content, rq_content_type):
        """
                ��������
        :param rq_content:�����������
        :param rq_content_type:str���ͣ���������
        """
        # ʹ�ô���Э��ģ���װ
        rq_ = CommunicationAgreementModel(rq_content, rq_content_type)
        rq_ = rq_.__repr__()
        self.__socket.send(rq_.encode('gbk'))

    def login(self, name, password):
        """
                ��¼����
        :param name:str���ͣ��û�����
        :param password:str���ͣ��û�����
        """
        # ��������������Ӧ���������ӷ���˻�ȡ������
        self.__send_rq((name, password), 'L')
        return self.__handle_rp()

    def register(self, name, password):
        """
                        ע�᷽��
        :param name:str���ͣ��û�����
        :param password:str���ͣ��û�����
        """
        # ��������������Ӧ���������ӷ���˻�ȡ������
        self.__send_rq((name, password), 'R')
        return self.__handle_rp()

    def exit(self):
        """
                        �˳�����
        """
        # ����������֪ͨ����˿ͻ����˳�
        self.__send_rq(None, 'Q')
        raise KeyboardInterrupt

    def seek_word(self, word_seek):
        """
                        ע�᷽��
        :param word_seek:str���ͣ�Ҫ���ҵĵ���
        """
        # ��������������Ӧ���������ӷ���˻�ȡ������
        self.__send_rq(word_seek, 'S')
        return self.__handle_rp()

    def show_history(self, bool_pretty_one):
        """
                        ע�᷽��
        :param bool_pretty_one:str���ͣ�'T' or 'F'
        """
        # ��������������Ӧ���������ӷ���˻�ȡ������
        self.__send_rq(bool_pretty_one == 'T', 'H')
        return self.__handle_rp()

    def quit(self):
        """
                        �˳�����
        """
        # ������������֪ͨ������û��˳�����Ϣ
        self.__send_rq(None, 'Q')


if __name__ == '__main__':
    test_agreement = CommunicationAgreementController()
    test_agreement.inet_connect()
