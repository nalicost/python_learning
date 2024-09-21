"""
                    队列模型
"""
# 顺序队列


class SQueue:
    def __init__(self, length=10):
        self.items = []
        self.length = length

    def enqueue(self, item):
        if self.is_full():
            raise IndexError
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) >= self.length


if __name__ == '__main__':
    queue = SQueue()
    for i in range(1, 11):
        queue.enqueue(i)
    # queue.enqueue(11)
    while not queue.is_empty():
        print(queue.dequeue())


# 链式队列
class Node01:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


# 有首位两个指针，首指针指向的是出列的，尾指针指向的是入列的，二者重合代表队列为空（其实留了一个元素）
class CQueue:
    def __init__(self, len_max=10):
        self.head = self.tail = Node01(None)
        # 先指向一个空的节点，方便后续移动
        self.len_max = len_max + 1

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return self.tell_len() >= self.len_max

    def tell_len(self):
        len_ = 0
        temp = self.head
        while True:
            try:
                temp = temp.next_node
            except AttributeError:
                return len_
            len_ += 1

    def enqueue(self, value):
        if self.is_full():
            raise IndexError
        self.tail.next_node = Node01(value)
        self.tail = self.tail.next_node

    def dequeue(self):
        if self.is_empty():
            raise IndexError
        self.head = self.head.next_node
        return self.head.value


if __name__ == '__main__':
    queue = CQueue()
    for i in range(1, 11):
        queue.enqueue(i)
    # queue.enqueue(11)
    while not queue.is_empty():
        print(queue.dequeue())
