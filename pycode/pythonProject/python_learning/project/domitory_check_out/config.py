"""
                寝室记账的配置文件
"""
# 调式模式
DEBUG = False
# mysql主机地址
HOST = 'localhost'
# mysql使用端口
PORT = 3306
# mysql用户名
USER_NAME = 'root'
# mysql密码
PASSWORD = 'Zjy20170132'
# 数据库名称
DATABASE = 'dormitory'
# 数据库文字编码
CHARSET = 'utf8'
# 使用用户元组
CLIENT = ('zyp', 'zjy', 'zhc', 'yjw') if not DEBUG else ('test', )
# 账单类型元组
TYPE = ('洗衣', '水费', '电费')
