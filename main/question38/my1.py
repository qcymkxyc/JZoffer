#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
    @Time :    18-12-15 上午11:53
    @Author:  qcymkxyc
    @File: my1.py
    @Software: PyCharm


"""
import copy


def whole_arrangement(s):
    """字符串全排列

    :param s: str
        字符串
    :return: List[str]
        所有全排列
    """
    all_arrangement = list()
    use_indexes = list()

    _arrangement(s, all_arrangement, use_indexes)

    return all_arrangement


def _arrangement(s, all_arrangement, use_indexes):
    """迭代循化函数

    :param s: str
        字符串
    :param all_arrangement: List[str]
        保存所有全排列可能
    :param use_indexes: List[int]
        已经用过的index
    """
    if len(use_indexes) == len(s):
        sub_s = "".join([s[i] for i in use_indexes])
        all_arrangement.append(sub_s)

    for i, ch in enumerate(s):
        if i in use_indexes:
            continue
        sub_use_indexes = copy.copy(use_indexes)
        sub_use_indexes.append(i)
        _arrangement(s, all_arrangement, sub_use_indexes)
