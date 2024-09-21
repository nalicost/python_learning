"""
                链表作业
"""


class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next_ = next_


class LinkList:
    def __init__(self):
        self.head = Node(None)

    def list_in_it(self, list_):
        tail = self.head
        for item in list_:
            tail = LinkList.iter_(tail, node_new=Node(item))[0]

    def show(self):
        tail = self.head.next_
        while tail:
            print(tail.value)
            tail = tail.next_

    def update(self, link_list_update):
        """
                更新
        :param link_list_update: 要更新的链表
        :return: 合并后的链表
        """
        link_list_new = LinkList()
        tail01, tail02, tail03 = self.head, link_list_update.head, link_list_new.head
        while tail02.next_:
            while tail01.next_ and tail01.next_.value <= tail02.next_.value:
                tail01 = tail01.next_
                tail03 = LinkList.iter_(tail03, node_new=Node(tail01.value))[0]
            tail02 = tail02.next_
            tail03 = LinkList.iter_(tail03, node_new=Node(tail02.value))[0]
        tail03.next_ = tail01.next_
        return link_list_new

    """合并实例
    def merge(l1, l2):
        # 思路:将l2并入l1，指针从l1头部移动，如果小于等于l2指针，就继续移动，大于则先用临时指针指向l1后续，然后将l1指针处连接l2指针，然后，l1
        # 指针替换为l2指针，l2指针替换为临时指针，接着重复
        tail01 = l1.head
        tail02 = l2.head.next_
        while tail01.next_:
            if tail01.next_.value <= tail02.value:
                tail01 = tail01.next_
            else:
                tem = tail01.next_
                tail01.next_ = tail02
                tail02, tail01 = tem, tail01.next_
        tail01.next_ = tail02
    """
    @staticmethod
    def iter_(*args, node_new=None):
        """
                链表迭代器
        :param args: 需迭代的节点
        :param node_new: 要加的新节点
        :return: 新节点所在的列表
        """
        re_list = []
        for node_old in args:
            if node_new:
                node_old.next_ = node_new
            re_list.append(node_old.next_)
        return re_list


a = LinkList()
b = LinkList()
a.list_in_it([2, 3, 5, 6, 7, 13, 15])
b.list_in_it([1, 2, 4, 9, 10, 16])
c = a.update(b)
c.show()
