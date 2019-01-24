#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
    @Time :    19-1-24 上午11:38
    @Author:  qcymkxyc
    @File: my2.py
    @Software: PyCharm
    
    题目二
"""


def repeat_num(nums):
    """

    :param nums:
    :return:
    """
    num_set = set()
    for num in nums:
        if num in num_set:
            return num
        else:
            num_set.add(num)

