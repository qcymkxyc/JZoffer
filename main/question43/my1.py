#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
    @Time :    19-1-15 上午10:50
    @Author:  qcymkxyc
    @File: my1.py
    @Software: PyCharm
    
    
"""


def count_1(n):
    """统计1出现的次数

    :param n: int
        n
    :return: int
        次数
    """
    count = 0
    for i in range(1, n + 1):
        s = str(i)
        if "1" in s:
            count += 1

    return count

