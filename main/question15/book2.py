#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 18-10-16 上午11:58
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : book2.py
@Software: PyCharm

书上最后一个解法
    
"""


def bin_count(num):
    """统计转换成的二进制中1的个数

    :param num: int
        十进制数
    :return: int
        1的个数
    """
    count = 0
    while num:
        count += 1
        num = (num - 1) & num

    return count
