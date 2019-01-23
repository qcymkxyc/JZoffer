#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
    @Time :    19-1-22 上午10:57
    @Author:  qcymkxyc
    @File: my1.py
    @Software: PyCharm


"""


def repeat_num(nums):
    """找出数组中重复数字

    :param nums: List[int]
        数组
    :return: int or None
        重复数字
    """
    if not nums:
        return

    hash_set = set()
    for num in nums:
        hash_num = hash(num)
        if hash_num in hash_set:
            return num
        else:
            hash_set.add(hash_num)
