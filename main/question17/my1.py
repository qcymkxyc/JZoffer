#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 18-10-20 上午10:44
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : my1.py
@Software: PyCharm
    
"""


def order_display(n):
    """顺序打印n位数

    :param n: int
        n位数
    :return : list
        打印结果
    """
    displays = list()
    num = 1
    while len(str(num)) <= n:
        displays.append(num)
        num += 1

    return displays
