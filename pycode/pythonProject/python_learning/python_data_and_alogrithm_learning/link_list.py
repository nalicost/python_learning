"""
                        单链表demo
"""
import time
# 第一种思路


class Node01:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
        # 通过将前一个创建的对象放入其中，形成节点（最后一个生成对象为起始节点，第一个生成对象为末节点）


# 演示,构建节点过程
node01 = Node01(1)
node02 = Node01(2, node01)
node03 = Node01(3, node02)
# 第二种思路


class Node02:
    def __init__(self, value):
        self.value = value
        self.next_node = None
        # 先预留下一个节点位置，后面赋值


# 演示,构建节点过程
# 缺点：稍微麻烦
node04 = Node02(1)
node05 = Node02(2)
node04.next_node = node05
node06 = Node02(3)
node05.next_node = node06
# 单链表生成
# 思路1，正向节点


class NodeList01:
    def __init__(self):
        self.head = Node02(None)

    def list_init(self, list_):
        tail = self.head
        for item in list_:
            tail.next_node = Node02(item)
            tail = tail.next_node

    def show(self):
        tail = self.head.next_node
        while tail is not None:
            print(tail.value)
            tail = tail.next_node

    def insert(self, index, value):
        new_node = Node02(value)
        tail = self.head
        for item in range(index):
            if tail.next_node:
                tail = tail.next_node
            else:
                break
        new_node.next_node = tail.next_node
        tail.next_node = new_node

    def delete(self, value):
        tail = self.head.next_node
        while tail.next_node and (f'{tail.next_node.value}' != f'{value}'):
            tail = tail.next_node
        if not tail.next_node:
            raise ValueError
        else:
            tail.next_node = tail.next_node.next_node

    def get_index(self, index):
        tail = self.head.next_node
        for item in range(index):
            if tail.next_node:
                tail = tail.next_node
            else:
                raise IndexError
        if index >= 0:
            return tail.value
        raise IndexError


# 思路二，逆向节点


class NodeList02:
    def __init__(self):
        self.head = Node01(None)

    def list_init(self, list_):
        for item in list_:
            self.head = Node01(item, self.head)


# node_list01 = NodeList01()
# list01 = [i for i in range(1000000)]
# time_start = time.time()
# for i in list01:
#     print(i)
# print(time.time() - time_start)
# node_list01.list_init(list01)
# time_start = time.time()
# node_list01.show()
# print(time.time() - time_start)
# l01 = range(1000000)
# time_start = time.time()
# for i in l01:
#     print(i)
# print(time.time() - time_start)
node_list02 = NodeList01()
node_list02.list_init(list(range(10)))
node_list02.insert(100, True)
node_list02.show()
print(node_list02.get_index(5))
node_list02.delete(True)
node_list02.show()
