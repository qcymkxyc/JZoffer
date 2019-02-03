#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
    @Time :    19-2-3 上午10:31
    @Author:  qcymkxyc
    @File: book1.py
    @Software: PyCharm
    
    
"""


def fibonacci(n):
    """斐波那契数列第n项结果

    :param n: int
        第n项
    :return: int
        第n项结果
    """
    temp1 = 0
    temp2 = 1
    for i in range(2, n + 1):
        f = temp1 + temp2
        temp1 = temp2
        temp2 = f

    return f
