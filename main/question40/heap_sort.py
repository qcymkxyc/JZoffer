#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
    @Time :    19-1-1 上午11:56
    @Author:  qcymkxyc
    @File: heap_sort.py
    @Software: PyCharm
    

"""


def _shift(nums, i, end = None):
    """"""
    if not end:
        end = len(nums)
    if i >= end:
        return False
    current_num = nums[i]
    left_index, right_index = 2 * i + 1, 2 * i + 2
    # if left child is not exist
    if left_index >= end:
        return False

    # search max child index
    max_child_index = left_index
    if right_index < end and nums[right_index] > nums[max_child_index]:
            max_child_index = right_index

    # exchange
    temp = nums[max_child_index]
    if current_num > nums[max_child_index]:
        return False
    else:
        nums[i], nums[max_child_index] = temp, current_num
        return True


def init_heap(nums, end):
    # init heap
    init_index = end // 2
    while init_index >= 0:
        # if exchange started from right child
        if _shift(nums, init_index, end):
            init_index = 2 * init_index + 2
            if init_index > end // 2:
                init_index == end // 2
            continue
        init_index -= 1


def heap_sort(nums):
    """

    :param nums: List[int]
    """
    end = len(nums)
    while end >= 1:
        init_heap(nums, end)
        nums[0], nums[end - 1] = nums[end - 1], nums[0]
        end -= 1



