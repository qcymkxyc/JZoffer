#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
    @Time :    19-1-24 上午10:27
    @Author:  qcymkxyc
    @File: my1.py
    @Software: PyCharm


"""


def max_value(matrix):
    """

    暴力解决
    :param matrix: List[List[int]]
        礼物矩阵
    :return: int
        最大价值的礼物
    """
    n_row, n_col = len(matrix), len(matrix[0])
    max_path_value = list()

    def _walk(current_coordinate=(0, 0), pre_value=0):
        """

        :param current_coordinate: (int, int)
            当前坐标
        :param pre_value: int
            之前的相加和
        """
        row, col = current_coordinate
        if row < 0 or row >= n_row:
            return
        if col < 0 or col >= n_col:
            return

        current_value = matrix[row][col]
        pre_value += current_value

        if row == n_row - 1 and col == n_col - 1:
            max_path_value.append(pre_value)
            return
        else:
            _walk((row + 1, col), pre_value)
            _walk((row, col + 1), pre_value)

    _walk()
    return max(max_path_value)
