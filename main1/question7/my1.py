#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
 @author:qcymkxyc
 @email:qcymkxyc@163.com
 @software: PyCharm
 @file: my1.py
 @time: 2019/1/30 14:51

"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left_child = None
        self.right_child = None


def pre_display(root):
    """前序遍历

    :param root: TreeNode
        树的根节点
    :return: List[int]
        前序遍历结果
    """
    if not root:
        return list()

    left_displays = pre_display(root.left_child)
    right_displays = pre_display(root.right_child)

    return [root.val] + left_displays + right_displays


def build_tree(pre_order, in_order):
    """重构二叉树

    :param pre_order: List[int]
        前序遍历
    :param in_order: List[int]
        中序遍历
    :return: TreeNode
        树的根节点
    """
    if set(pre_order)!= set(in_order):
        raise ValueError("元素不一致")
    if len(pre_order) != len(in_order):
        raise ValueError("长度不等")

    if len(pre_order) == 0:
        return

    root_val = pre_order[0]

    in_left_traversal = in_order[:in_order.index(root_val)]
    in_right_traversal = in_order[in_order.index(root_val) + 1:]

    pre_left_traversal = list(filter(lambda x: x in in_left_traversal, pre_order))
    pre_right_traversal = list(filter(lambda x: x in in_right_traversal, pre_order))

    node = TreeNode(root_val)
    node.left_child = build_tree(pre_left_traversal, in_left_traversal)
    node.right_child = build_tree(pre_right_traversal, in_right_traversal)

    return node
