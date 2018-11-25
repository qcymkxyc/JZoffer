#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 上午11:37
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : my2.py
@Software: PyCharm

32题的扩展题目

"""


def breadth_first_search(adjacency_matrix):
    """广度优先遍历

    :param adjacency_matrix: np.array
        邻接矩阵
    :return: list
        遍历顺序
    """
    displays = list()
    if adjacency_matrix is None:
        return displays

    queue = list()
    queue.append(0)

    while len(queue) != 0:
        current_index = queue.pop(0)
        # 如果已经浏览过则跳过该节点
        if current_index in displays:
            continue

        displays.append(current_index)

        for adjacency_index, v in enumerate(adjacency_matrix[current_index]):
            if v != 0:
                queue.append(adjacency_index)

    return displays
