#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
    @Time :    19-1-11 上午10:48
    @Author:  qcymkxyc
    @File: book1.py
    @Software: PyCharm


"""


def max_sub_nums(nums):
    """最大和的连续子数组

    :param nums: List[int]
        数组
    :return: List[int],int
        子数组,和
    """
    # 空数组
    if len(nums) == 0:
        return nums,0

    # 如果全是负数
    if len(list(filter(lambda x: x < 0, nums))) == len(nums):
        return [], 0

    max_sum = 0
    pre_sum = 0
    start, end = 0, len(nums) - 1
    for i, num in enumerate(nums):
        if pre_sum + num <= num:
            start = i
            pre_sum = num
        else:
            pre_sum += num

        if pre_sum > max_sum:
            max_sum = pre_sum
            end = i

    return nums[start: end + 1], max_sum
