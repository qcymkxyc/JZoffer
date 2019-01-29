#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
    @Time :    19-1-29 上午10:51
    @Author:  qcymkxyc
    @File: book1.py
    @Software: PyCharm
    
    
"""


def first_once_ch(s):
    """第一个只出现一次的字母

    :param s: str
        字符串
    :return: str
        字母
    """
    hash_dict = dict()
    for i,ch in enumerate(s):
        hash_ch = hash(ch)
        hash_dict.setdefault(hash_ch, 0)
        hash_dict[hash_ch] += 1

    for ch in s:
        hash_ch = hash(ch)
        if hash_dict[hash_ch] == 1:
            return ch