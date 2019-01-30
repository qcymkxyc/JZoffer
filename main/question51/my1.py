#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
    @Time :    19-1-30 上午10:26
    @Author:  qcymkxyc
    @File: my1.py
    @Software: PyCharm


"""


def reverse_tuple(nums):
    """逆序对

    :param nums: List[int]
        数组
    :return: int
        逆序对的个数
    """
    count = 0
    for i, num1 in enumerate(nums):
        for j in range(i, len(nums)):
            num2 = nums[j]
            if num1 > num2:
                count += 1

    return count
