#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    18-12-6 上午11:51
@Author:  qcymkxyc
@File: my1.py
@Software: PyCharm


"""


def search_tree_2_list(root):
    """搜索树转双向链表

    :param root: BinaryTreeNode
        树的根结点
    :return: BinaryTreeNode
        链表头节点
    """
    if not root:
        return None

    root.left_child = search_tree_2_list(root.left_child)

