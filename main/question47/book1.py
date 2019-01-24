#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
    @Time :    19-1-24 上午10:58
    @Author:  qcymkxyc
    @File: book1.py
    @Software: PyCharm
    
    
"""


def max_value(matrix):
    """

    动态规划
    :param matrix: List[List[int]]
        矩阵
    :return: int
        最大值
    """
    n_row, n_col = len(matrix), len(matrix[0])

    value_matrix = list()
    for i, v in enumerate(matrix):
        value_matrix.append([0] * len(v))

    # 第一行初始化
    for i in range(n_col):
        value_matrix[0][i] += sum(matrix[0][:i + 1])

    # 第一列初始化
    for row in range(n_row):
        value_matrix[row][0] = sum(map(lambda x:x[0], matrix[:row + 1]))

    for row in range(1,n_row):
        for col in range(1,n_col):
            value_matrix[row][col] = max(value_matrix[row - 1][col], value_matrix[row][col - 1]) + \
                matrix[row][col]

    return value_matrix[-1][-1]
