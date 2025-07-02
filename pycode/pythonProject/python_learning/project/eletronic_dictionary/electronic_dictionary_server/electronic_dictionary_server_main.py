# -*- encoding:gbk -*-
"""
                        此模块为电子词典服务端的主模块
"""
from electronic_dictionary_server_communication_agreement_bll import *
if __name__ == '__main__':
    bll_main = CommunicationAgreementController()
    # 主模块入口
    bll_main.main()
