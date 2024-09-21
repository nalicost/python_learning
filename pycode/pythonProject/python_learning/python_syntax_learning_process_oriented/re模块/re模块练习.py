"""
                    匹配端口状态（无文本）
"""
import re


class MessageServer:
    def __init__(self, file_name=None):
        self.file_name = file_name
        self.file_content = self.__get_file()

    def __get_file(self):
        try:
            with open(f'{self.file_name}') as f:
                return f.read()
        except FileNotFoundError:
            print('文件不存在')
            self.file_name = input('请输入存在的正确文件：')
            return self.__get_file()

    def main(self):
        while True:
            try:
                port = input('你要寻找的端口是：')
                print(self.__get_port_address(port))
            except Exception:
                print('端口不存在')
                continue

    def __get_port_address(self, port_):
        obj = re.search(rf'\n{port_}\b', self.file_content)
        pos_start = obj.start()
        sub = re.compile(r'address is (?P<addr>\S+)')
        result = sub.search(self.file_content, pos_start)
        return result.group('addr')


if __name__ == '__main__':
    ms = MessageServer('test_port.txt')
    ms.main()
