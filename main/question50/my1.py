#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
    @Time :    19-1-29 上午10:25
    @Author:  qcymkxyc
    @File: my1.py
    @Software: PyCharm


"""
from collections import OrderedDict


def first_once_ch(s):
    """第一个只出现一次的字母

    :param s: str
        字符串
    :return: str
        字母
    """
    hash_dict = OrderedDict()
    for i, ch in enumerate(s):
        hash_dict.setdefault(ch, 0)
        hash_dict[ch] += 1

    for k, v in hash_dict.items():
        if v == 1:
            return k
