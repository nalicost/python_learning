# -*- encoding:gbk -*-
"""
                        ��ģ��Ϊ���Ӵʵ����ģ��
"""
import sys
# ���·����ʹ������pycharm��Ҳ������
sys.path.append(r'C:\Users\zhang\PycharmProjects\pythonProject\python_learning\project'
                r'\eletronic_dictionary\electronic_dictionary_client')
from electronic_dictionary_client_ui import *
if __name__ == '__main__':
    test_ui = ElectronicDictionaryUI()
    # ���������
    test_ui.main()
