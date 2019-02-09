#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
    @Time :    19-2-9 上午10:47
    @Author:  qcymkxyc
    @File: book1.py
    @Software: PyCharm


"""


def pair_nums(nums, s):
    """合为s的数字对

    :param nums: List[int]
        数组
    :param s: int
        s
    :return: (int, int)
        数字对
    """
    if not nums:
        return

    left, right = 0, len(nums) - 1
    while left < right:
        num1 = nums[left]
        num2 = nums[right]

        if num1 + num2 == s:
            return num1, num2
        elif num1 + num2 > s:
            right = right - 1
        else:
            left = left + 1
