#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
    @Time :    19-2-9 上午11:05
    @Author:  qcymkxyc
    @File: my2.py
    @Software: PyCharm
    
    
"""


def sum_seq(s):
    """所有合为s的正序序列

    :param s: int
        s
    :return: List[List[int]]
        所有正序序列
    """
    start, end = 1, 2
    seqs = list()
    while end < s:
        seq = range(start, end + 1)
        num = sum(seq)
        if num == s:
            seqs.append(list(seq))
            end += 1
        elif num < s:
            end += 1
        else:
            start += 1

    return seqs
