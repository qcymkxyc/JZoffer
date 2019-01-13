#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
    @Time :    19-1-13 上午11:15
    @Author:  qcymkxyc
    @File: question2.py
    @Software: PyCharm

    给定一个矩阵ｍ，从左上角开始每次只能向右或者向下走，最后到达右下角的位置
    路径上所有的数字累加起来就是路径和，返回所有的路径中最小的路径和。
"""
import pprint
m = [
    [1, 3, 5, 9],
    [8, 1, 3, 4],
    [5, 0, 6, 1],
    [8, 8, 4, 0]
]


def min_path(matrix):
    """最小路径

    :param matrix: List[List[int]]
        矩阵
    :return: int
    """
    n_row, n_col = len(matrix), len(matrix[0])
    # 初始化最小值矩阵
    min_matrix = []
    for i in range(n_row):
        min_matrix.append([0] * n_col)

    # 第一行初始化
    for i, v in enumerate(matrix[0]):
        min_matrix[0][i] = sum(matrix[0][:i]) + v

    # 第一列初始化
    col_0 = list(map(lambda x: x[0], matrix))
    for i in range(n_row):
        v = col_0[i]
        min_matrix[i][0] = sum(col_0[:i]) + v

    # 计算最小路径
    for row in range(1, n_row):
        for col in range(1, n_col):
            v = matrix[row][col]
            min_matrix[row][col] = min(min_matrix[row - 1][col], min_matrix[row][col - 1]) + v

    for i in min_matrix:
        print(i)
    return min_matrix[-1][-1]
