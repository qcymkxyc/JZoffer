#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
    @Time :    19-1-28 上午11:25
    @Author:  qcymkxyc
    @File: my1.py
    @Software: PyCharm


"""


def find_num(matrix, num):
    """查找数

    :param matrix: List[List[int]]
        矩阵
    :param num: int
        要查找的数
    :return: bool
        是否存在
    """
    n_row, n_col = len(matrix), len(matrix[0])

    for col in range(n_col - 1, -1, -1):
        least_num = matrix[0][col]
        if num < least_num:
            continue
        else:
            for row in range(n_row):
                c_num = matrix[row][col]
                if c_num == num:
                    return True
            return False
