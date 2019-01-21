#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 上午11:31
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : my1.py
@Software: PyCharm

"""


def is_post_order(root, post_seq):
    """判断序列是否是一棵树的后序遍历

    :param root: BinaryTreeNode
        树的根结点
    :param post_seq: list
        后序遍历
    :return: bool
        是否是后序遍历
    """
    return _post_display(root) == post_seq


def _post_display(root):
    """后序遍历

    :param root: BinaryTreeNode
        树的根结点
    :return: list
        后序遍历
    """
    displays = list()
    if not root:
        return displays

    displays.extend(_post_display(root.left_child))
    displays.extend(_post_display(root.right_child))
    displays.append(root.val)

    return displays
