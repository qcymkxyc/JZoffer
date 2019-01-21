#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 18-10-16 上午11:42
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : book1.py
@Software: PyCharm

书上是用移位运算解决(移位运算的效率高于除法),该方式可能出现四循环
    
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
        if num & 1:
            count += 1
        num = num >> 1

    return count
