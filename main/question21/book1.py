#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 18-10-24 上午11:35
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : book1.py
@Software: PyCharm

书上的解法相当于快速排序
    
"""


def adjust_list(nums):
    """调整nums的顺序使奇数位于偶数之前

    类似于快速排序的思想

    :param nums: list or tuple
        原始数组
    """
    start, end = 0, len(nums) - 1

    while start < end:
        # 左侧循环
        while nums[start] % 2 == 1:
            start += 1
        # 右侧循环
        while nums[end] % 2 == 0:
            end -= 1

        nums[end], nums[start] = nums[start], nums[end]
        end -= 1
        start += 1

