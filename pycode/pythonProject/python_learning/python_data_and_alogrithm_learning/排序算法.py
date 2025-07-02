"""
                    排序算法
"""
# 冒泡算法


def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# 选择排序


def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                arr[min_index], arr[j] = arr[j], arr[min_index]


#  插入排序


def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break


# 快速排序
def sub_sort(head, tail, arr):
    x = arr[head]
    # 确定基准值
    while head < tail:
        # 循环结束条件：由于确定基准后从两侧根据大小移放，故当收尾相接时，全部排序完成
        while arr[tail] > x:
            # 从后向前，大的留住，小的放置左侧空位
            tail -= 1
        arr[head] = arr[tail]
        # 交换空位，空位变为右侧
        while arr[head] <= x and head < tail:
            # 从前往后，小的留住，大的放右侧空位
            head += 1
        arr[tail] = arr[head]
        # 交换空位，空位变为左侧
    arr[head] = x
    # 插入基准值
    return head
    # 返回分割点


def quick_sort(head, tail, arr):
    if head < tail:
        # 结束条件：每次递归会传入新的头和尾，当头尾相接结束递归
        key = sub_sort(head, tail, arr)
        # 返回新的分割点
        quick_sort(head, key - 1, arr)
        # 传回分割点左侧数组
        quick_sort(key + 1, tail, arr)
        # 传回分割点右侧数组


if __name__ == '__main__':
    list_ = [1, 2, 4, 3, 9, 10]
    # bubble_sort(list_)
    # selection_sort(list_)
    # insertion_sort(list_)
    quick_sort(0, len(list_) - 1, list_)
    print(list_)
