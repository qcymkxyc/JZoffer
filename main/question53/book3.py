#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
    @Time :    19-2-2 上午11:53
    @Author:  qcymkxyc
    @File: book3.py
    @Software: PyCharm
    
    
"""


def index_equal_num(nums):
    """找出数值和下标相等的元素

    :param nums: List[int]
        数组
    :return: int
        元素
    """
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        mid_num = nums[mid]

        if mid_num > mid:
            right = mid - 1
        elif mid == mid_num:
            return mid
        else:
            left = mid + 1
