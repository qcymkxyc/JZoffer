#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
    @Time :    18-12-17 上午11:21
    @Author:  qcymkxyc
    @File: book3.py
    @Software: PyCharm

    相关题目
"""


def sum_equal(seq):
    """正方体和相等的排列

    :param seq: List[int]
        数组
    :return: List[List[int]]
        相等的排列
    """
    equal_arrangement = list()
    arrangement = _all_arrangement(seq)
    for arr in arrangement:
        if is_right_seq(arr):
            equal_arrangement.append(arr)
    return equal_arrangement


def is_right_seq(seq):
    """判断是否是符合规定的数组

    :param seq: List[int]
        数组
    :return: bool
        是否符合规定
    """
    if sum(seq[:4]) != sum(seq[4:]):
        return False
    if sum(filter(lambda x: seq.index(x) % 2 == 1, seq)) != \
            sum(filter(lambda x: seq.index(x) % 2 == 0, seq)):
        return False
    index1 = [0, 1, 4, 5]
    index2 = [2, 3, 6, 7]
    if sum([seq[i] for i in index1]) != sum([seq[i] for i in index2]):
        return False

    return True


def _all_arrangement(seq):
    """该数组的所有排列

    :param seq: List[int]
        数组
    :return: List[List[int]]
    `   所有排列
    """
    import copy

    def inner_arrangement(arrangement, use_seq):
        if len(use_seq) == len(seq):
            arrangement.append(use_seq)
            return

        for i, val in enumerate(seq):
            if val in use_seq:
                continue
            temp_seq = copy.copy(use_seq)
            temp_seq.append(val)
            inner_arrangement(arrangement,temp_seq)

    arrange = list()
    inner_arrangement(arrangement=arrange, use_seq=list())
    return arrange
