# 本代码都是通过二分查找算法解决问题的，注：由于函数注释后来才明确要写，故仅添加一个函数解释作为参考
nul = [20, 33, 78, 25, 52, 50, 22, 20, 59, 37, 31, 23, 2, 97, 79, 14, 9, 63, 36, 85, 46, 71, 65, 69, 74, 59, 14, 85, 98,
       37, 24, 88, 16, 71, 44, 18, 62, 45, 42, 52, 94, 46, 35, 76, 97, 41, 18, 93, 66, 44]
nul.sort()


# 方法一：由于拿不出经过递归最后的返回值，所以通过传入list可变类型数据记录最后的结果
# result = [False] #默认false
# def seek_01( nul_0, list_0, list_index, list_len_max, list_len_min, result): #定义函数，传入内容分别为要找的数字，原列表，查找位置，已确认的最大位置，已确认的最小位置，结果接收
#     if abs(list_len_min - list_len_max) == 1 : #递归终止条件，查找到底了
#         result = [bool(list_0[list_len_min] == nul_0 or list_0[list_len_max] == nul_0)]
#     elif list_0[list_index - 1] != nul_0 : #找不到，则继续往下查找
#         output = [(list_len_max + list_index) // 2, list_index, list_len_max] if list_0[list_index - 1] < nul_0 else [
#             (list_len_min + list_index) // 2, list_len_min, list_index] #三元赋值，如果找到的值小了说明一定比这个位置的数大，故将已确认最小位置修改，反之亦然
#         seek_01(nul_0, list_0, output[0], output[2], output[1] ,result) #找不到则继续函数递归
#     else: #找到了，修改可变类型数据结果，变为true
#         result[0] = True
# nul_ = int(input(':>'))
# n = seek_01(nul_, nul, (len(nul) - 1) // 2 , len(nul) - 1 , 0, result)
# print(result[0])


# 方法二，与上方思路相同，不同的是，可以通过return递归函数的结果，将最后一层递归结果返回至表层
def seek_01(nul_0, list_0, list_index, list_len_max, list_len_min=0):
    """
                            二分查找算法，递归查值
    :param nul_0: 需查找的值
    :param list_0: 查找的列表对象
    :param list_index: 初始查找的位置，一般为中间
    :param list_len_max: 查找列表的最大索引
    :param list_len_min: 查找列表的最小索引，默认为0
    :return: bool
    """
    if abs(list_len_min - list_len_max) == 1:  # 递归停止条件
        return list_0[list_len_min] == nul_0 or list_0[list_len_max] == nul_0
    elif list_0[list_index - 1] != nul_0:
        output = ((list_len_max + list_index) // 2, list_index, list_len_max) if list_0[list_index - 1] < nul_0 else \
                    ((list_len_min + list_index) // 2, list_len_min, list_index)
        return seek_01(nul_0, list_0, output[0], output[2], output[1])  # 通过改return来递归函数，并将结果递归会表层
    else:  # 递归找到结果
        return True


nul_ = int(input(':>'))
n = seek_01(nul_, nul, (len(nul) - 1) // 2, len(nul) - 1)
print(n)

# 方法三：结果返回表层方式于上方相同，算法实现方式不同
# def binary_search(lis, left, right, num):
#     if left > right:#递归结束条件
#         return -1
#     mid = (left + right) // 2 #直接找中间值
#     if num < lis [mid]:
#         right = mid -1 #大了，将最大值修改为其左侧一位
#     elif num > lis[mid]:
#         left = mid + 1 #小了，将最小值修改为其右侧一位
#     else:
#         return mid
#     return binary_search(lis, left, right, num)
# lis = [11, 32, 51, 21, 42, 9, 5, 6, 7, 8]
# lis.sort()
# num = int(input('输入要查找的数：'))
# res = binary_search(lis, 0, len(lis)-1, num)
# if res == -1:
#     print('未找到！')
# else:
#     print('找到！')
