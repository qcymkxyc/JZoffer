#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 18-10-13 上午10:53
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : my1.py
@Software: PyCharm
    
"""


def edge_check(matrix, current_coordinate):
    """边界检查

    检查当前坐标是否合法（比如col小于0或者col大于matrix的col）

    :param matrix: tuple(row,col)
        方格的行和列数，即row * col
    :param current_coordinate: tuple（row，col）
        当前坐标
    :return: bool
        如果当前坐标不合法返回False，否则返回True
    """
    row, col = current_coordinate
    matrix_row, matrix_col = matrix

    if row >= matrix_row or row < 0:
        return False
    if col < 0 or col >= matrix_col:
        return False

    return True


def num_check(current_coordinate, k):
    """数位检验

    检测当前坐标数位之和是否小于等于k

    :param current_coordinate: tuple(row,col)
        当前坐标
    :param k: int
        k
    :return: bool
        是否小于k
    """
    row, col = current_coordinate
    num_sum = 0

    # 计算数位和
    temp = row
    while temp > 0:
        num_sum += temp % 10
        temp = int(temp / 10)
    temp = col
    while temp > 0:
        num_sum += temp % 10
        temp = int(temp / 10)

    if num_sum <= k:
        return True
    return False


def init_visit_matrix(matrix_shape):
    """初始化是否访问的矩阵

    :param matrix_shape: tuple(row,col)
        矩阵形状
    :return: list
         是否访问的list
    """
    matrix_row, matrix_col = matrix_shape

    is_visit = []
    for i in range(matrix_row):
        is_visit.append([False] * matrix_col)

    return is_visit


def matrix_search(matrix_shape, current_coordinate, k, is_visit_matrix = None):
    """矩阵搜索

    在矩阵中搜索数位和小于k的坐标，并统计坐标个数

    分以下几种情况：
    1. 符合要求
        需统计个数加1，并且朝四个方向再次迭代
    2. 不符合要求
        2.1 当前坐标越界
        2.2 当前坐标访问过
        2.3 当前坐标数值和大于k

    :param matrix_shape: tuple(row,col)
        矩阵形状
    :param current_coordinate: tuple(row,col)
        搜索的起始坐标
    :param k: int
        k
    :param is_visit_matrix: list
        表示是否已经访问过的矩阵
    :return: int
        统计的坐标个数
    """
    # 初始化是否访问矩阵
    if not is_visit_matrix:
        is_visit_matrix = init_visit_matrix(matrix_shape)

    # 检测不符合要求的情况
    # 越界
    if not edge_check(matrix_shape, current_coordinate):
        return 0

    # 已经访问过
    current_row, current_col = current_coordinate
    if is_visit_matrix[current_row][current_col]:
        return 0

    # 是否坐标数值小于等于k
    if not num_check(current_coordinate, k):
        return 0

    # 符合要求的情况
    is_visit_matrix[current_row][current_col] = True
    count = 1

    # 移动的四个方向
    moves = [
        (current_row - 1, current_col),     # 上
        (current_row + 1, current_col),     # 下
        (current_row, current_col - 1),     # 左
        (current_row, current_col + 1)      # 右
    ]
    for move_coodinate in moves:
        count += matrix_search(matrix_shape, move_coodinate, k, is_visit_matrix)

    return count
