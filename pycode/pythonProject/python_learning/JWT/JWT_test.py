import base64
import hmac
import copy
import json
import time


class JWT:
    def __init__(self):
        pass

    @staticmethod
    def my_b64_en(en_str):
        re_str = base64.urlsafe_b64encode(en_str)
        # 将占位符等号清空
        re_str = re_str.replace(b'=', b'')
        return re_str

    @staticmethod
    def my_b64_de(de_str):
        # 计算缺少的占位符
        len_str_mod = len(de_str) % 4
        fill_char_len = 4 - len_str_mod if len_str_mod > 0 else 0
        de_str = de_str + fill_char_len * b'='
        re_str = base64.urlsafe_b64decode(de_str)
        return re_str

    @staticmethod
    def encode(en_dic, exp):
        # 头部转json串
        header_ori = json.dumps({'alg': 'SHA256', 'typ': 'JWT'}, separators=(',', ':'), sort_keys=True)
        # 转为b串
        header = JWT.my_b64_en(header_ori.encode())
        # 深copy防止污染原字典
        dic = copy.deepcopy(en_dic)
        # 防止exp获取的内容无法转int
        if not (isinstance(exp, int) or isinstance(exp, str)):
            raise TypeError
        # 增加过期时间
        dic['exp'] = int(exp) + time.time()
        # payload转json串
        payload_ori = json.dumps(dic, separators=(',', ':'), sort_keys=True)
        # payload转b串
        payload = JWT.my_b64_en(payload_ori.encode())
        # 生成hmac对象
        res = hmac.new(key=b'hiIAmZJY', msg=header + b'.' + payload, digestmod='SHA256')
        # 生成签名
        signature = JWT.my_b64_en(res.digest())
        # 返回最终b串，即token
        return header + b'.' + payload + b'.' + signature

    @staticmethod
    def decode(de_str):
        # 分割token，分别获取header，payload，signature
        de_li = de_str.split(b'.')
        # 二次计算的签名
        sig_con = hmac.new(key=b'hiIAmZJY', msg=de_li[0] + b'.' + de_li[1], digestmod='SHA256').digest()
        # 确认token是否被串改
        if JWT.my_b64_de(de_li[2]) == sig_con:
            # 获取payload内容，转为字典
            re_dic = json.loads(JWT.my_b64_de(de_li[1]).decode())
            # 查看是否超时
            if re_dic['exp'] < time.time():
                return {'msg': '过时了', 're_sta': False}
            return {'msg': re_dic, 're_sta': True}
        return {'msg': '签名根本不是我', 're_sta': False}


if __name__ == '__main__':
    re = JWT.encode({'name': 'user', 'pass': '12345'}, 300)
    print(re)
    print(JWT.decode(re))
    print(JWT.decode(b'eyJhbGciOiJTSEEyNTYiLCJ0eXAiOiJKV1QifQ.eyJleHAiOjE3NDg0NDU3MzEuNjczMzE5LCJuYW1lIjoidXNlciIsInBhc3MiOiIxMjM0NSJ9.zMY9_TICx9LA3GXGZ7ZP17cQz3OYd-rgXw95scozKyk'))
    re = JWT.encode({'name': 'user', 'pass': '12345'}, -200)
    print(JWT.decode((re)))
