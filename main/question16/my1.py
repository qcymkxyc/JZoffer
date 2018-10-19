#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 18-10-19 上午11:29
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : my1.py
@Software: PyCharm
    
"""


def power(base, exponent):
    """求base的exponent次方

    考虑两种可能性：
    1. exponent为正数
    2. exponent为负数

    :param base: float
        base
    :param exponent: int
        次方
    :return: float
        运算结果
    """
    # 判断exponent是否为负数
    is_negative = exponent < 0

    if is_negative:
        exponent = -exponent

    base_exponent = 1   # 保存的运算结果
    for i in range(1, exponent + 1):
        base_exponent *= base

    if is_negative:
        base_exponent = 1. / base_exponent

    return base_exponent
