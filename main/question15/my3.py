#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 18-10-16 下午12:13
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : my3.py
@Software: PyCharm

书上的相关题目1

"""


def power_2(num):
    """判断该数是否是2的整数次方

    :param num: int
        要判断的数
    :return: bool
        是否是2的整数次方
    """
    return not bool(num & (num - 1))