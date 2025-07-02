# -*- encoding:gbk -*-
"""
                        此模块为电子词典的主模块
"""
import sys
# 添加路径，使得脱离pycharm，也可运行
sys.path.append(r'C:\Users\zhang\PycharmProjects\pythonProject\python_learning\project'
                r'\eletronic_dictionary\electronic_dictionary_client')
from electronic_dictionary_client_ui import *
if __name__ == '__main__':
    test_ui = ElectronicDictionaryUI()
    # 主函数入口
    test_ui.main()
