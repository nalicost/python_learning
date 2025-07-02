"""
                    二叉树练习
"""
from 队列模型 import SQueue


class BinaryTreeNode:
    """
        二叉树节点
    """
    def __init__(self, value, left_node=None, right_node=None):
        self.value = value
        self.left_node = left_node
        # 左孩子
        self.right_node = right_node
        # 右孩子


class BinaryTree:
    def __init__(self, value=None):
        self.root_ = BinaryTreeNode(value)
        self.layer_list = [self.root_]
        # 用来记录还有空余的节点
        self.dir = -1
        # 用来记录第一个空余节点的左右孩子的赋值情况

    def add_node(self, *args):
        for item01 in range(len(args)):
            if self.dir == -1:
                temp = self.layer_list[0].left_node = BinaryTreeNode(args[item01])
                # 左孩子赋值
            else:
                temp = self.layer_list[0].right_node = BinaryTreeNode(args[item01])
                # 右孩子赋值
                del self.layer_list[0]
                # 清空赋值满的节点
            self.dir = -self.dir
            # 表示节点的空满情况
            self.layer_list.append(temp)
            # 增加新节点

    @staticmethod
    def preorder(root_):
        if root_ is None:
            return
        print(root_.value, end=' ')
        # 打印根节点
        BinaryTree.preorder(root_.left_node)
        # 走左支
        BinaryTree.preorder(root_.right_node)
        # 走右支

    @staticmethod
    def postorder(root_):
        if root_ is None:
            return
        BinaryTree.postorder(root_.left_node)
        # 走左支
        BinaryTree.postorder(root_.right_node)
        # 走右支
        print(root_.value, end=' ')
        # 打印根节点

    @staticmethod
    def in_order(root_):
        if root_ is None:
            return
        BinaryTree.in_order(root_.left_node)
        # 走左支
        print(root_.value, end=' ')
        # 打印根节点
        BinaryTree.in_order(root_.right_node)
        # 走右支

    @staticmethod
    def level_order(*args, re_list):
        for item02 in args:
            print(item02.value, end=' ')
            # 打印该层节点值
            if item02.left_node:
                re_list.append(item02.left_node)
                # 增加该节点下一层的左孩子
            if item02.right_node:
                re_list.append(item02.right_node)
                # 增加该节点下一层的右孩子
        if not args:
            # 元组为空，结束
            return
        BinaryTree.level_order(*re_list, re_list=[])

    # 队列非递归实现
    @staticmethod
    def level_order_(root_):
        re_queue = SQueue()
        re_queue.enqueue(root_)
        while not re_queue.is_empty():
            node_root_ = re_queue.dequeue()
            print(node_root_.value, end=' ')
            if node_root_.left_node:
                re_queue.enqueue(node_root_.left_node)
            if node_root_.right_node:
                re_queue.enqueue(node_root_.right_node)


if __name__ == '__main__':
    list_ = ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    item = BinaryTree('a')
    item.add_node(*list_)
    item.preorder(item.root_)
    print()
    item.in_order(item.root_)
    print()
    item.postorder(item.root_)
    print()
    item.level_order(item.root_, re_list=[])
    print()
    item.level_order_(item.root_)
