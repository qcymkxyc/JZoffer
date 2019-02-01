#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
 @author:qcymkxyc
 @email:qcymkxyc@163.com
 @software: PyCharm
 @file: my1.py
 @time: 2019/2/1 14:37

"""


class BinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left_child = None
        self.right_child = None
        self.parent = None


def create_binary_tree(pre_order, in_order):
    """创建二叉树

    :param pre_order: List[int]
        前序遍历
    :param in_order: List[int]
        中序遍历
    :return: BinaryTreeNode
        树的根节点
    """
    if set(pre_order) != set(in_order):
        raise ValueError
    if len(pre_order) != len(in_order):
        raise ValueError
    if len(pre_order) == 0:
        return None
    if len(pre_order) == 1:
        return BinaryTreeNode(pre_order[0])

    root_val = pre_order[0]

    in_left_child = in_order[:in_order.index(root_val)]
    in_right_child = in_order[in_order.index(root_val) + 1:]

    pre_left = list(
        filter(
            lambda x: x in in_left_child,pre_order))
    pre_right = list(filter(lambda x: x in in_right_child, pre_order))

    root = BinaryTreeNode(root_val)
    left_child_node = create_binary_tree(pre_left, in_left_child)
    right_child_node = create_binary_tree(pre_right, in_right_child)

    root.left_child = left_child_node
    root.right_child = right_child_node
    if left_child_node:
        left_child_node.parent = root
    if right_child_node:
        right_child_node.parent = root

    return root


def pre_display(root):
    """ 前序遍历

    :param root: BinaryTreeNode
        树的根节点
    :return: List[int]
        遍历结果
    """
    if not root:
        return list()

    return [root.val] + pre_display(root.left_child) + pre_display(root.right_child)


def in_display(root):
    """中序遍历

    :param root: BinaryTreeNode
        树的根节点
    :return: List[int]
        遍历结果
    """
    if not root:
        return list()

    return in_display(root.left_child) + \
        [root.val] + in_display(root.right_child)


def in_order_next_node(c_node):
    """中序遍历的下一个节点

    1.当前节点没有右子树
        1.1 当前节点是父节点的左子树
        1.2 当前节点是父节点的右子树
    2.当前节点有右子树
    :param c_node: BinaryTreeNode
        当前节点
    :return: BinaryTreeNode
        下一个节点
    """
    # 当前节点为空
    if not c_node:
        return None

    # 有右子树
    if c_node.right_child:
        return c_node.right_child

    # 无右子树
    # 当前节点是父节点的左子树
    if c_node == c_node.parent.left_child:
        return c_node.parent
    else:   # 当前节点是父节点的右子树
        temp_node = c_node.parent
        while temp_node:
            if temp_node == temp_node.parent.left_child:
                return temp_node.parent
            temp_node = temp_node.parent
