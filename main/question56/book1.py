#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
 @author:qcymkxyc
 @email:qcymkxyc@163.com
 @software: PyCharm
 @file: book1.py
 @time: 2019/2/8 11:07

"""


def _single_unique_num(nums):
    """找出一个不重复数字

    :param nums: List[int]
        数组
    :return: int
        不重复数字
    """
    n = 0
    for v in nums:
        n = n ^ v

    return n


def _find_first_index(num):
    if num == 0:
        return
    index = 0
    while num:
        index += 1
        num = num >> 1
        if num & 1 == 1:
            break

    return index


def _get_first_bit_num(index):
    num = 1
    for i in range(index):
        num = num << 1

    return num


def unique_num(nums):
    """找出两个不重复的数字

    :param nums: Lint[int]
        数组
    :return: int,int
        不重复数字
    """
    n = 0
    for v in nums:
        n = v ^ n
    first_index = _find_first_index(n)
    temp_num = _get_first_bit_num(first_index)

    num1, num0 = 0, 0
    for v in nums:
        if v & temp_num:
            num1 = num1 ^ v
        else:
            num0 = num0 ^ v

    return num1, num0
