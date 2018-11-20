#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 上午11:07
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : my1.py
@Software: PyCharm

"""
from collections import OrderedDict
import numpy as np


def _is_legal_point(matrix, point):
    """判定是否是合法的坐标

    1. 判断该坐标是否已经走过（走过表示为None）
    2. 判断当前坐标是否越界（小于0或者大于矩阵长宽）

    :param matrix: np.array
        矩阵
    :param point: tuple(int, int)
        坐标
    :return: bool
        是否合法
    """
    point_row, point_col = point
    n_row, n_col = matrix.shape

    # 判断当前坐标是否越界
    if point_row >= n_row or point_row < 0:
        return False
    if point_col >= n_col or point_col < 0:
        return False

    # 判断是否已经走过（走过标记为None）
    if matrix[point_row][point_col] == np.inf:
        return False

    return True


def clockwise_display(matrix, last_direction="right", current_point=(0, 0)):
    """顺时针打印矩阵

    该函数使用迭代方式实现，当前节点下一次所走方向与上一节点所走
    方向一致，如果该方向上的节点已经走过，则依照右下左上的顺序改
    变方向，如若四个方向都已经走过则停止迭代

    :param matrix: np.array
        要打印的矩阵
    :param current_point: tuple(int, int)
        当前节点
    :param last_direction: str
        上一次迭代所走的方向
    :return: list
        打印的list
    """
    displays = list()
    # 如果当前节点不合法
    if not _is_legal_point(matrix, current_point):
        return displays

    current_row, current_col = current_point
    displays.append(matrix[current_row][current_col])
    matrix[current_row][current_col] = np.inf   # 已走过的标记为无穷大

    # 下一次所走的右下左上四个方向
    direction_keys = ["right", "down", "left", "up"]
    directions = OrderedDict()
    directions["right"] = (current_row, current_col + 1)
    directions["down"] = (current_row + 1, current_col)
    directions["left"] = (current_row, current_col - 1)
    directions["up"] = (current_row - 1, current_col)

    # 把上一走的方向放在第一个
    while direction_keys[0] != last_direction:
        temp_direct = direction_keys.pop(0)
        direction_keys.append(temp_direct)
    for direction in direction_keys:
        point = directions[direction]
        if _is_legal_point(matrix, point):
            displays.extend(clockwise_display(matrix, direction, point))
            break

    return displays
