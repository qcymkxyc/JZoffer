#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
    @Time :    18-12-31 下午12:37
    @Author:  qcymkxyc
    @File: book1.py
    @Software: PyCharm


"""
from . import heap_sort


def get_least_num1(nums, k):
    """书上的解法一"""
    pass


def get_least_num2(nums, k):
    """书上的解法二"""
    if k > len(nums):
        raise IndexError

    import copy
    # 初始化前k个并排序
    heap_nums = copy.copy(nums[:k])
    heap_sort.heap_sort(heap_nums)

    # 后面的数字依次加入比较
    for i in range(k, len(nums)):
        current_num = nums[i]
        max_heap_num = heap_nums[-1]
        if current_num < max_heap_num:
            heap_nums[-1] = current_num
            heap_sort.heap_sort(heap_nums)

    return heap_nums
