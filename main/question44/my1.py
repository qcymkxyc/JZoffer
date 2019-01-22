#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
    @Time :    19-1-22 上午10:08
    @Author:  qcymkxyc
    @File: my1.py
    @Software: PyCharm


"""


def find_num(i):
    """寻找第i位对应的数字

    :param i: int
        index
    :return: int
        数字
    """
    num = 0
    n = 0
    while n <= i:
        s_num = str(num)
        s = s_num[-1]
        n += len(s_num)
        num += 1

    return int(s)
