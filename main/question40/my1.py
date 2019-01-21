#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
    @Time :    18-12-31 下午12:11
    @Author:  qcymkxyc
    @File: my1.py
    @Software: PyCharm


"""


def bubble_min(nums, k):
    """利用冒泡找最小的k个数

    :param nums: List[int]
        候选数组
    :param k: int
        最小的k个数
    :return: List[int]
    """
    if k > len(nums):
        raise ValueError("k过大")

    for i in range(k):
        for j in range(len(nums) - 1, i, -1):
            num1, num2 = nums[j], nums[j - 1]
            if num1 < num2:
                nums[j], nums[j - 1] = num2, num1

    return nums[:k]
