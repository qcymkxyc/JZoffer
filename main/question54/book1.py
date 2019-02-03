#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
    @Time :    19-2-3 上午10:12
    @Author:  qcymkxyc
    @File: book1.py
    @Software: PyCharm


"""


def k_num(root, k):
    """二叉搜索树的第k大的节点

    :param root: BinaryTreeNode
        树的根节点
    :param k: int
        第k大
    :return: BinaryTreeNode
        第k大的节点
    """
    def _in_order(root):
        """中序遍历"""
        if not root:
            return []
        return _in_order(root.left_child) + \
            [root.val] + _in_order(root.right_child)

    if k <= 0:
        raise ValueError("k值错误")
    return _in_order(root)[k - 1]
