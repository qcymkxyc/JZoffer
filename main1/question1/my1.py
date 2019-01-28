#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
 @author:qcymkxyc
 @email:qcymkxyc@163.com
 @software: PyCharm
 @file: my1.py
 @time: 2019/1/21 11:42

"""

matrix = [
    [1, 2, 8, 9],
    [2, 4, 9, 12],
    [4, 7, 10, 13],
    [6, 8, 11, 15]
]


def find_num(matrix, num):
    """查找该数

    :param matrix: List[List[int]]
        矩阵
    :param num: int
        查找的数
    :return: bool
        是否存在
    """
    n_row, n_col = len(matrix), len(matrix[0])

    row, col = 0, 0
    while True:
        n = matrix[row][col]
        if n < num:
            row += 1
            col += 1
        elif n == num:
            return True
        else:

