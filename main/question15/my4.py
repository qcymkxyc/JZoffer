#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 18-10-16 下午12:19
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : my4.py
@Software: PyCharm

相关题2

"""


def transform_count(m, n):
    """求m的二进制形式改变多少位才能得到n

    :param m: int
        m
    :param n: int
        n
    :return: int
        改编的位数
    """
    # 异或求取不同位数
    diff_bin = m ^ n

    # 统计位数
    count = 0
    while diff_bin:
        count += 1
        diff_bin = (diff_bin - 1) & diff_bin

    return count
