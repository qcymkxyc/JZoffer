#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 上午11:35
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : book1.py
@Software: PyCharm

"""


def level_display(root):
    """层次打印

    :param root: BinaryTreeNode
        树的根结点
    :return: list
        层次打印序列
    """
    displays = list()   # 打印队列
    assist_list = list()    # 辅助队列

    # 根结点为空
    if not root:
        return displays

    assist_list.append(root)
    while len(assist_list) != 0:
        node = assist_list.pop(0)
        if not node:
            continue
        displays.append(node.val)
        assist_list.extend([node.left_child, node.right_child])

    return displays
