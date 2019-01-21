#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 18-11-4 上午11:15
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : my1.py
@Software: PyCharm

"""


def reverse_tree(root):
    """反转树

    利用递归交换左右子树

    :param root: BinaryTreeNode
        树的根节点
    """
    if not root:
        return

    # 反转子树
    reverse_tree(root.left_child)
    reverse_tree(root.right_child)

    # 反转该结点
    root.left_child, root.right_child = root.right_child, root.left_child
