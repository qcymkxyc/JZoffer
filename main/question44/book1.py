#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
    @Time :    19-1-22 上午10:23
    @Author:  qcymkxyc
    @File: book1.py
    @Software: PyCharm
    
    
"""


def find_num(i):
    """查找数字

    :param i: int
        index
    :return: int
        数字
    """
    n = 0
    j = 1   # 次方
    while n < i:
        if j == 1:
            ns = 10 ** j
        else:
            ns = 10 ** j - 10 ** (j - 1)
        ns_len = ns * j
        if n + ns_len > i:
            nf = (i - n) / j
            nf_b = (i - n) % j
            num = 10 ** (j - 1) + nf
            s = str(num)[nf_b]
            break
        else:
            n += ns_len

    return int(s)

