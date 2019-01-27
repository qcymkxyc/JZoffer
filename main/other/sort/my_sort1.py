#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 18-9-30 上午10:31
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : my_sort1.py
@Software: PyCharm

排序练习

"""
import copy


def quick_sort(nums):
    """快速排序

    :param nums: list or tuple
        输入序列
    :return: list
        排序结果
    """
    # TODO 未完成
    sort_list = copy.copy(list(nums))

    def patition(nums, start, end):
        """

        :param nums:
        """
        pass


def bubble_sort(nums):
    """冒泡排序(正序)

    :param nums: list or tuple
        输入序列
    """
    for i in range(0, len(nums) - 2):
        for j in range(len(nums) - 1, i, -1):
            val1, val2 = nums[j - 1], nums[j]
            if val2 < val1:
                nums[j], nums[j - 1] = val1, val2


def insert_sort(nums):
    """直接插入排序

    :param nums: list or tuple
        输入序列
    """
    for j in range(1, len(nums)):
        temp = nums[j]

        i = j - 1
        while temp < nums[i] and i >= 0:
            nums[i + 1] = nums[i]
            i -= 1
        nums[i + 1] = temp


def binary_insert_sort(nums):
    """二分插入排序

    :param nums: list or tuple
        输入序列
    """
    def binary_search(start, end, search_value):
        """二分查找

            查找该数在数列中的位置

        :param start: int
            开始index
        :param end: int
            结束index
        :param search_value:int or float
            要查找的数字
        :return: int
            search_value在序列中的index（插入排序不会出现找不到的情况）
        """
        left, right = start, end
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < search_value:
                left = mid + 1
            else:
                right = mid - 1
        return left

    for j in range(1, len(nums)):
        temp = nums[j]

        i = j - 1
        index = binary_search(0, i, temp)
        for k in range(j, index, -1):
            nums[k] = nums[k - 1]
        nums[index] = temp


def merge_sort(nums):
    """归并排序

    :param nums: list or tuple
        需要排序的数组
    """
    def merge(nums1, nums2):
        """归并

        :param nums1: list or tuple
            合并数组1
        :param nums2: list or tuple
            合并数组2
        :return: list
            合并后的数组
        """
        merge_nums = list()
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                merge_nums.append(nums1[i])
                i += 1
            else:
                merge_nums.append(nums2[j])
                j += 1

        merge_nums.extend(nums1[i:])
        merge_nums.extend(nums2[j:])

        return merge_nums

    if len(nums) <= 1:
        return nums

    mid = (len(nums)) // 2
    left_nums = nums[: mid]
    right_nums = nums[mid:]

    left_nums = merge_sort(left_nums)
    right_nums = merge_sort(right_nums)

    return merge(left_nums, right_nums)


def select_sort(nums):
    """选择排序

    :param nums : list or tuple
        待排序的数组
    """
    for i in range(len(nums)):
        current_num = nums[i]

        min_num = current_num
        min_index = i
        for j in range(i, len(nums)):
            if nums[j] < min_num:
                min_num = nums[j]
                min_index = j
        # 交换
        nums[i] = min_num
        nums[min_index] = current_num


def radix_sort1(nums):
    """基数排序

    :param nums: list
        待排序数列
    :return: list
        排序后的数列
    """
    def init_table():
        """
        初始化排序表
        :return: list
            排序表,排序表中一共有10个子列表，用index识别他们对应的分组
        """
        table = list()
        for i in range(0, 10):
            table.append([])
        return table

    max_len_num = max(nums, key=lambda x: len(str(x)))  # 获取最大位数
    max_len = len(str(max_len_num))

    for digit in range(max_len):
        table = init_table()  # 初始化分组列表
        for num in nums:
            str_num = str(num)
            try:
                index = eval(str_num[-1 - digit])  # 获得最后digit对应的数，也即index
            except IndexError:  # 排除位数不够的情况
                index = 0
            finally:
                table[index].append(num)
        # 重新合并
        nums = list()
        for sub_nums in table:
            nums.extend(sub_nums)

    return nums


class Node:
    """
        单链表结点
    """

    def __init__(self, num=None):
        self.data = num
        self.next_node = None


class LinkList:
    """
        链表
    """

    def __init__(self, head_node=None):
        self.head = head_node
        self.tail = head_node

    def append(self, node):
        """
            添加元素
        :param node: 结点
        :raises:
            TypeError : node的不为结点类型
        """
        if not isinstance(node, Node):
            raise TypeError()

        if self.head is None and self.tail is None:
            self.head, self.tail = node, node
        else:
            self.tail.next_node = node
            self.tail = node

    def traverse(self):
        """遍历链表
            :return:list
                遍历列表
        """
        traverse_list = list()
        current_node = self.head
        while current_node:
            traverse_list.append(current_node.data)
            current_node = current_node.next_node
        return traverse_list


def radix_sort2(nums):
    """基数排序

        链表实现基数排序

    :param nums:list
        待排序数组
    :return: list
        数组
    """
    max_len_num = max(nums, key=lambda x: len(str(x)))
    max_len = len(str(max_len_num))

    for digit in range(max_len):
        # 初始化列表
        table = list()
        for i in range(10):
            table.append(LinkList())

        for num in nums:
            try:
                index = eval(str(num)[-1 - digit])
            except IndexError:
                index = 0
            finally:
                node = Node(num)
                table[index].append(node)

        # 重新合并
        nums = list()
        for link_list in table:
            nums.extend(link_list.traverse())

    return nums


def shell_sort(nums):
    """希尔排序

    :param nums: list
        待排序数组
    """
    def insert_sort(nums, start_index, interval):
        """直接插入排序

        :param nums: list
            待排序数组
        :param start_index: int
            开始排序index
        :param interval: int
            希尔跳跃间隔
        """
        for i in range(start_index + interval, len(nums), interval):
            x = nums[i]

            j = i
            while j > start_index:
                temp = nums[j - interval]
                if x > temp:
                    break
                nums[j] = temp
                j = j - interval
            nums[j] = x

    n_num = len(nums)
    interval = n_num // 2

    # 外层循环循环间隔
    while interval >= 1:
        # 内层循环循环子序列
        for start in range(n_num):
            if start / n_num >= 1:
                break
            insert_sort(nums, start, interval)  # 对子序列直接插入排序
        interval -= 1
