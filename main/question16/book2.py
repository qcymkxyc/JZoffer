#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 18-10-19 下午12:24
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : book2.py
@Software: PyCharm
    
"""


def power(base, exponent):
    """求base的exponent次方

    该函数在此基础上用递归实现，使时间复杂度变为O(logn)

    :param base: int
        base
    :param exponent: float
        exponent
    :return: float
        结果
    :raises:
        ZeroDivisionError: base为0且exponent为负数
    """
    is_negative = exponent < 0  # 是否是负数
    abs_exponent = -exponent if is_negative else exponent   # 指数的绝对值

    # 考虑0的情况
    if base == 0 and is_negative:
        raise ZeroDivisionError("不能base为0且exponent为负数")

    base_exponent = power_abs_exponent(base, abs_exponent)

    # 负数情况
    if is_negative:
        base_exponent = 1. / base_exponent

    return base_exponent


def power_abs_exponent(base, abs_exponent):
    """计算base的abs_exponent次方（abs_exponent为正数）

    :param base: float
        base（正常情况）
    :param abs_exponent: int
        exponent(正数或0)
    :return:
    """
    if abs_exponent == 0:
        return 1
    if abs_exponent == 1:
        return base

    # 判断指数是否为奇数
    is_exponent_odd = abs_exponent % 2

    base_abs_exponent = power_abs_exponent(base, abs_exponent // 2) ** 2
    base_abs_exponent = base_abs_exponent * base if is_exponent_odd else base_abs_exponent

    return base_abs_exponent
