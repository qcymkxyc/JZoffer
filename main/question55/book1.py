#!usr/bin/env python 
# -*- coding:utf-8 _*-  
""" 
 @author:qcymkxyc
 @email:qcymkxyc@163.com
 @software: PyCharm
 @file: book1.py
 @time: 2019/2/4 11:07
 
"""


def tree_depth(root):
    """树的深度

    :param root: BinaryTreeNode
        树的根节点
    :return: int
        深度
    """
    if not root:
        return 0

    left_depth = tree_depth(root.left_child)
    right_depth = tree_depth(root.right_child)

    return max(left_depth, right_depth) + 1
