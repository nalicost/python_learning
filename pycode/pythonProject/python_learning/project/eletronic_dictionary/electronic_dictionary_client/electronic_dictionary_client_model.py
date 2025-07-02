# -*- encoding:gbk -*-
"""
            ��ģ��Ϊ���Ӵʵ�ͻ��˵�����ģ�ͣ����а�������Э������ģ�ͺͲ˵�������ģ���Լ��ڵ�ģ��
"""


class NodeModel:
    """
                ˫��ڵ���
    """
    def __init__(self, value, degree):
        """
                ��ʼ��ʵ������
        :param value:��ǰ�ڵ��ֵ
        :param degree:�ڵ������ӽڵ�
        """
        self.node = value
        # �����ӽڵ㣬��һ������Ҫ�游�ڵ�
        self.degree = self.origin_set_degree(degree + 1)

    @staticmethod
    def origin_set_degree(value):
        """
                ��ʼ�����ӽڵ��ֵ
        :param value:��ǰ�ڵ��ֵ
        :return:
        """
        # ������յļ���ռλ���ӽڵ�
        return [NodeModel(None, -1) for i in range(value)]


class CommunicationAgreementModel:
    """
                ����Э����
    """
    def __init__(self, content, content_type):
        """
                ��ʼ��ʵ������
        :param content:��������
        :param content_type:�������Ӧ������
        """
        self.content = content
        self.content_type = content_type

    def __repr__(self):
        """
                �����ַ�����ʽ����
        """
        # ���Ϊ�ַ����ټ����ţ���ֹexalʱ����
        if isinstance(self.content, str):
            return f"CommunicationAgreementModel('{self.content}', '{self.content_type}')"
        else:
            return f"CommunicationAgreementModel({self.content}, '{self.content_type}')"


class MenuModel:
    """
                �༶�˵���
    """
    def __init__(self, origin_value, max_degree):
        """
                ��ʼ��ʵ������
        :param origin_value:�˵��ĳ�ʼֵ
        :param max_degree: �ڵ��������
        """
        # ���ڵ�洢
        self.root_node = NodeModel(origin_value, max_degree)
        # ��ǰ�����Ľڵ�洢
        self.now_node = self.root_node
        # ��¼��ǰ����
        self.layer = 1
        self.__max_degree = max_degree
        # ��ǰδ�洢���Ľڵ����
        self.__degree_now = 1
        # ��ǰ�ӽڵ�δ�洢���Ľڵ�
        self.__layer_list = [self.root_node]

    def add_node_order_by_layer(self, target_list_value):
        """
                ���ղ������ӽڵ�
        :param target_list_value:���ղ������е�ֵ
        """
        for item_0 in target_list_value:
            obj = NodeModel(item_0, self.__max_degree)
            if self.__degree_now > self.__max_degree:
                # ��һ���ڵ���ӽڵ�ȫ���洢��ɺ�ɾ���ڵ㲢����δ�洢�Ķ���λ��
                del self.__layer_list[0]
                self.__degree_now = 1
            # ���ӽڵ㸳ֵ
            self.__layer_list[0].degree[self.__degree_now] = obj
            # ���ӽڵ�ĸ��ڵ㸳ֵ
            obj.degree[0] = self.__layer_list[0]
            # ����δ�洢���ӽڵ�Ľڵ㣬���¼�����ӽڵ�
            self.__layer_list.append(obj)
            # �ڵ�δ�洢�Ķ���λ�ú���
            self.__degree_now += 1

    def select_path(self, choice=0):
        """
                ����ѡ���·��
        :param choice:int���ͣ�ѡ���·��
        :return:ѡ��·���ڵ��ֵ
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
