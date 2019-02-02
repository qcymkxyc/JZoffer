#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
    @Time :    19-2-2 上午10:12
    @Author:  qcymkxyc
    @File: my1.py
    @Software: PyCharm


"""
import math


def _binary_search1(nums, num):
    """二分查找

    :param nums: List[int]
        数组
    :param num: int
        数字
    :return: int
        待查数字的位置
    """
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        mid_num = nums[mid]

        if mid_num == num:
            return mid
        elif mid_num > num:
            right = mid - 1
        else:
            left = mid + 1

    return math.inf


def num_time1(nums, num):
    """数字出现次数

    二分查找
    :param nums: List[int]
        数组
    :param num: int
        数字
    :return: int
        出现次数
    """
    num_index = _binary_search1(nums, num)

    if num_index == math.inf:
        return 0
    count = 0
    # 向左找
    for i in range(num_index, -1, -1):
        if nums[i] != num:
            break
        count += 1

    # 向右找
    for i in range(num_index + 1, len(nums)):
        if nums[i] != num:
            break
        count += 1

    return count


def _binary_search2(nums, num):
    left, right = 0, len(nums) - 1
    count = 0
    while left <= right:
        mid = (left + right) // 2
        mid_num = nums[mid]

        if mid_num == num:
            count += 1
            count += _binary_search2(nums[:mid], num)
            count += _binary_search2(nums[mid + 1:], num)
            break
        elif num < mid_num:
            right = mid - 1
        else:
            left = mid + 1

    return count


def num_time2(nums, num):
    """数字出现次数

    二分查找
    :param nums: List[int]
        数组
    :param num: int
        数字
    :return: int
        出现次数
    """
    return _binary_search2(nums, num)
