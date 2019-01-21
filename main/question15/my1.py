#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 18-10-16 上午11:18
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : my1.py
@Software: PyCharm

运用内置的函数求得
    
"""


def bin_count(num):
    """求一个十进制数转换为2进制后1的个数

    :param num: int
        十进制数
    :return: int
        1的个数
    :raises:
        TypeError: num不为int
    """
    if not isinstance(num, int):
        raise TypeError("数字必须为int型")
    bin_num = bin(num)

    count = 0
    for ch in bin_num:
        if ch == "1":
            count += 1

    return count
