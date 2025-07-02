"""
        接收的服务类型
"""
from views import *
# 路由列表
urls_list = [('/time', get_time), ('/bye', bye), ('/hello', hello)]

# 加入可以接受的服务，使得网页请求内容多样化
