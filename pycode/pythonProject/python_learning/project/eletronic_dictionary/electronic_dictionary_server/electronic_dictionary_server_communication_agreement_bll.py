# -*- encoding:gbk -*-
"""
                ��ģ��Ϊ���Ӵʵ����˵�ҵ���߼�ģ�飬���а���������Ӧ�Ĵ��������ݿ��ȡ�߼������ģ�͵�����
"""
from electronic_dictionary_server_database_bll import *
import socket
import threading


# �̳��߳��࣬ʹ�ÿ���ֱ�ӵ���start��ʵ�ִ�������
class CommunicationAgreementController(threading.Thread):
    """
                    ���紫��Э���߼���
    """
    # �������̼߳��룬�����̣߳��ͷ���Դ
    threading_list = []

    def __init__(self, addr=('127.0.0.1', 10090), socket_target=None):
        """
                    ��ʼ��ʵ������
        :param addr: tuple���ͣ�����������󶨵ĵ�ַ
        :param socket_target: default��None������Ŀͻ����׽���
        """
        super().__init__()
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__addr = addr
        self.__socket_client = socket_target
        # �����洢���ӿͻ����û�������
        self.__user = None
        # �����洢��װ��������
        self.__service_dict = {'L': self.__login, 'R': self.__register, 'E': self.__exit,
                               'S': self.__seek_word, 'H': self.__show_history, 'Q': self.__quit}
        # ��ϸ������ݿ�����߼�ģ��
        self.database_controller = DatabaseController()

    def __set_server_sock(self):
        """
                    �����������
        """
        self.__socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.__socket.bind(self.__addr)
        self.__socket.listen(3)

    def __handle_rq(self):
        """
                    �������󣬵���ѡ����񷽷�
        """
        self.__choice_service()

    def __send_rp(self, rq_content, rq_content_type):
        """
                    ������Ӧ
        :param rq_content: ��Ӧ�ľ�������
        :param rq_content_type: str���ͣ���Ӧ������
        """
        # ��װ�����紫��Э������
        rq_ = CommunicationAgreementModel(rq_content, rq_content_type)
        # �����ַ������ͣ����д���
        rq_ = rq_.__repr__()
        self.__socket_client.send(rq_.encode('gbk'))

    def __choice_service(self):
        """
                    ����ѡ�񷽷�
        """
        # ���տͻ��˵�����
        data = self.__socket_client.recv(1024).decode('gbk')
        # �Ͽ����ӣ����˳��߳�
        if not data:
            raise BrokenPipeError
        # ���յ������������紫��Э�����
        rq_ = eval(data)
        # �����������ͣ����ú���
        self.__service_dict[rq_.content_type](rq_)

    def __login(self, rq_target):
        """
                    ��¼����
        :param rq_target:�������
        """
        # ��ȡ�������ݣ����������ݿ��߼�ģ���ô�����
        content_re, content_state = self.database_controller.login(rq_target.content)
        # ��ȡ�ɹ���������û�
        if content_re:
            self.__user = rq_target.content[0]
        # ������Ӧ���ͷ���
        self.__send_rp(content_re, content_state)

    def __register(self, rq_target):
        """
                    ע�᷽��
        :param rq_target:�������
        """
        content_re, content_state = self.database_controller.register(rq_target.content)
        self.__send_rp(content_re, content_state)

    def __exit(self, *args):
        """
                    �˳�����
        :param args:��������ò���
        """
        # �����˳��߳�
        raise BrokenPipeError

    def __seek_word(self, rq_target):
        """
                    ���ҵ��ʷ���
        :param rq_target:�������
        """
        # ��ȡ�������ݣ����������ݿ����߼���ȡ������
        content_re, content_state = self.database_controller.seek_word(rq_target.content, self.__user)
        # ������Ӧ���ͷ���
        self.__send_rp(content_re, content_state)

    def __show_history(self, rq_target):
        """
                    �鿴��ʷ��¼����
        :param rq_target:�������
        """
        # ��ȡ�������ݣ����������ݿ����߼���ȡ������
        content_re, content_state = self.database_controller.show_history(rq_target.content, self.__user)
        # ������Ӧ���ͷ���
        self.__send_rp(content_re, content_state)

    def __quit(self, *args):
        """
                    ��¼����
        :param args:����Ĳ���
        """
        # �û��˳������ر��̣߳������û�����Ϊ��
        self.__user = None

    def run(self):
        """
                    �̴߳���ͻ�������
        """
        # ѭ�����տͻ�����iȥ
        while True:
            try:
                self.__handle_rq()
            # �����˳�
            except BrokenPipeError:
                break

    def main(self):
        """
                    ������
        """
        # �����������
        self.__set_server_sock()
        # �����������̻߳��շ�������ʹ�����߳��˳�����һ���˳�
        handle_t = threading.Thread(target=threading_handle, daemon=True)
        handle_t.start()
        # ѭ�����տͻ�������
        while True:
            try:
                socket_client, addr = self.__socket.accept()
                print('Connect from', addr)
                # Ϊ�ͻ�������ר���߳�
                thread_client = CommunicationAgreementController(socket_target=socket_client)
                thread_client.start()
                # �ڻ����߳������Ӵ����߳�
                CommunicationAgreementController.threading_list.append(thread_client)
            # �˳�������
            except KeyboardInterrupt:
                break
            # ��ֹ�������쳣�˳�
            except Exception as e:
                print(e)


def threading_handle():
    """
            �̻߳��պ���
    """
    # ��ѭ������
    while True:
        # �����̻߳����б�
        for i in CommunicationAgreementController.threading_list:
            # �ж��߳��Ƿ������
            if not i.is_alive():
                # ɾ��������߳�
                CommunicationAgreementController.threading_list.remove(i)
            # �����߳�
            i.join(20)


if __name__ == '__main__':
    test_agreement = CommunicationAgreementController()
    test_agreement.main()

