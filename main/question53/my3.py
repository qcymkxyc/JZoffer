#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
    @Time :    19-2-2 上午11:48
    @Author:  qcymkxyc
    @File: my3.py
    @Software: PyCharm


"""


def index_equal_num(nums):
    """找出数值和下标相等的元素

    :param nums: List[int]
        数组
    :return: int
        元素
    """
    for i, v in enumerate(nums):
        if v == i:
            return v
