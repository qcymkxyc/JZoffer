#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 18-10-19 下午12:07
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : book1.py
@Software: PyCharm
    
"""


def power(base, exponent):
    """求base的exponent次方

    书上在考虑正数和负数的基础上还考虑了0的因素

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

    base_exponent = 1
    for i in range(1, abs_exponent + 1):
        base_exponent *= base

    # 负数的情况
    if is_negative:
        base_exponent = 1. / base_exponent

    return base_exponent
