#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 18-10-16 上午11:26
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : my2.py
@Software: PyCharm

不用内置函数
    
"""


def transform2bin(num):
    """转换为二进制数

    :param num: int
        十进制数
    :return: str
        二进制数
    """
    temp = num

    str_bin = ""    # 保存转换成二进制的str形式
    while temp >= 2:
        remainder = temp % 2
        temp = int(temp / 2)
        str_bin = str(remainder) + str_bin
    str_bin = str(temp) + str_bin

    return str_bin


def bin_count(num):
    """统计转换成的二进制中1的个数

    :param num: int
        十进制数
    :return: int
        1的个数
    """
    # 转换成二进制
    str_bin = transform2bin(num)

    count = 0
    for ch in str_bin:
        if ch == "1":
            count += 1

    return count
