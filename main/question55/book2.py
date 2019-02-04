#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
 @author:qcymkxyc
 @email:qcymkxyc@163.com
 @software: PyCharm
 @file: book2.py
 @time: 2019/2/4 11:17

"""
from . import book1


def is_balance_tree(root):
    """判断是否是平衡二叉树

    :param root: BinaryTreeNode
        树的根节点
    :return: bool
        是否是平衡二叉树
    """
    if not root:
        return True

    if not (is_balance_tree(root.left_child) and
            is_balance_tree(root.right_child)):
        return False

    left_depth = book1.tree_depth(root.left_child)
    right_depth = book1.tree_depth(root.right_child)
    if abs(left_depth - right_depth) > 1:
        return False
    return True
