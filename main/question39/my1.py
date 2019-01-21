#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
    @Time :    18-12-19 下午12:10
    @Author:  qcymkxyc
    @File: my1.py
    @Software: PyCharm


"""
from operator import itemgetter


def max_count_num(seq):
    """最多数字个数的数字

    :param seq: List[int]
        数组
    :return: int
        数字
    """
    if len(seq) == 0:
        raise ValueError("seq为空")

    count_dict = dict()
    for i, num in enumerate(seq):
        count_dict.setdefault(num, 0)
        count_dict[num] += 1

    return sorted(count_dict.items(), key=itemgetter(1), reverse=True)[0][0]
