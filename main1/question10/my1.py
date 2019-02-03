#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
    @Time :    19-2-3 上午10:26
    @Author:  qcymkxyc
    @File: my1.py
    @Software: PyCharm
    
    
"""


def fibonacci(n):
    """斐波那契数列第n项结果

    :param n: int
        第n项
    :return: int
        第n项结果
    """
    if n == 0 or n == 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)
