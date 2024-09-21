"""
                栈模型
"""
# 顺序存储的栈


class SStack:
    def __init__(self):
        self.stack_ = []

    def is_empty(self):
        return len(self.stack_) == 0

    def push(self, item):
        self.stack_.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError
        return self.stack_.pop()

    def top(self):
        if self.is_empty():
            raise IndexError
        return self.stack_[-1]


# 链式栈
class Node01:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


class ChainStack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top

    def push(self, item):
        self.top = Node01(item, self.top)

    def pop(self):
        if not self.is_empty():
            raise IndexError
        temp = self.top
        self.top = self.top.next_node
        return temp

    def top_show(self):
        if self.is_empty():
            raise IndexError
        return self.top


if __name__ == '__main__':
    chain_stack = ChainStack()
    chain_stack.push(1)
    chain_stack.push(2)
    chain_stack.push(3)
    print(chain_stack.pop().value)
    print(chain_stack.pop().value)
    print(chain_stack.pop().value)
    # print(chain_stack.pop().value)
