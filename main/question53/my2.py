#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
    @Time :    19-2-2 上午11:28
    @Author:  qcymkxyc
    @File: my2.py
    @Software: PyCharm
    
    
"""


def miss_num(nums):
    """缺失的数字

    :param nums: List[int]
        数组
    :return: int
        缺失的数字
    """
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        mid_num = nums[mid]

        if mid_num == mid:
            left = mid + 1
        else:
            right = mid
    if right == len(nums) - 1:
        raise ValueError("无缺失")
    return right
