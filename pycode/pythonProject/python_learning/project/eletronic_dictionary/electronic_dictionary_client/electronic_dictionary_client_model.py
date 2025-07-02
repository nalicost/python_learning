# -*- encoding:gbk -*-
"""
            本模块为电子词典客户端的数据模型，其中包含传输协议数据模型和菜单的数据模型以及节点模型
"""


class NodeModel:
    """
                双向节点类
    """
    def __init__(self, value, degree):
        """
                初始化实例变量
        :param value:当前节点的值
        :param degree:节点的最多子节点
        """
        self.node = value
        # 生成子节点，加一是由于要存父节点
        self.degree = self.origin_set_degree(degree + 1)

    @staticmethod
    def origin_set_degree(value):
        """
                初始设置子节点的值
        :param value:当前节点的值
        :return:
        """
        # 将多个空的几点占位其子节点
        return [NodeModel(None, -1) for i in range(value)]


class CommunicationAgreementModel:
    """
                传输协议类
    """
    def __init__(self, content, content_type):
        """
                初始化实例变量
        :param content:传输内容
        :param content_type:请求或响应的类型
        """
        self.content = content
        self.content_type = content_type

    def __repr__(self):
        """
                返回字符串形式的类
        """
        # 如果为字符串再加引号，防止exal时出错
        if isinstance(self.content, str):
            return f"CommunicationAgreementModel('{self.content}', '{self.content_type}')"
        else:
            return f"CommunicationAgreementModel({self.content}, '{self.content_type}')"


class MenuModel:
    """
                多级菜单类
    """
    def __init__(self, origin_value, max_degree):
        """
                初始化实例变量
        :param origin_value:菜单的初始值
        :param max_degree: 节点的最大度数
        """
        # 根节点存储
        self.root_node = NodeModel(origin_value, max_degree)
        # 当前遍历的节点存储
        self.now_node = self.root_node
        # 记录当前层数
        self.layer = 1
        self.__max_degree = max_degree
        # 当前未存储到的节点度数
        self.__degree_now = 1
        # 当前子节点未存储满的节点
        self.__layer_list = [self.root_node]

    def add_node_order_by_layer(self, target_list_value):
        """
                依照层序增加节点
        :param target_list_value:按照层序排列的值
        """
        for item_0 in target_list_value:
            obj = NodeModel(item_0, self.__max_degree)
            if self.__degree_now > self.__max_degree:
                # 当一个节点的子节点全部存储完成后，删除节点并重置未存储的度数位置
                del self.__layer_list[0]
                self.__degree_now = 1
            # 给子节点赋值
            self.__layer_list[0].degree[self.__degree_now] = obj
            # 给子节点的父节点赋值
            obj.degree[0] = self.__layer_list[0]
            # 增加未存储满子节点的节点，即新加入的子节点
            self.__layer_list.append(obj)
            # 节点未存储的度数位置后移
            self.__degree_now += 1

    def select_path(self, choice=0):
        """
                返回选择的路径
        :param choice:int类型，选择的路径
        :return:选择路径节点的值
        """
        self.now_node = self.now_node.degree[choice]
        self.layer = self.layer + 1 if choice != 0 else self.layer - 1
        return self.now_node.node


if __name__ == '__main__':
    list_test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    test_menu_model = MenuModel(0, 3)
    test_menu_model.add_node_order_by_layer(list_test)
    print(test_menu_model.root_node.degree[1].degree[1].node)
    comm_test = CommunicationAgreementModel('nihao', 'p')
    print(comm_test.content, comm_test.content_type, comm_test.__repr__())
