#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
    @Time :    18-12-14 上午11:37
    @Author:  qcymkxyc
    @File: my1.py
    @Software: PyCharm
    
    
"""
import pickle
from main.question26 import my1 as q26


def serialize_binary_tree(root):
    """序列化二叉树

    :param root: BinaryTreeNode
         树的根结点
    :return: bytes
        pickle序列化后的结果
    """
    level_traverse = level_display(root)
    return pickle.dumps(level_traverse)


def deserialize_binary_tree(level_traverse):
    """反序列化

    :param level_traverse: bytes
        序列化结果
    :return: BinaryTreeNode
        树的根结点
    """
    level_traverse = pickle.loads(level_traverse)
    # 为空
    if not level_traverse:
        return

    level_traverse = list(map(lambda val: q26.BinaryTreeNode(val) if val else None, level_traverse))
    for i, node in enumerate(level_traverse):
        if not node:
            continue
        left_index = (i + 1) * 2 - 1
        right_index = (i + 1) * 2

        if left_index < len(level_traverse):
            node.left_child = level_traverse[left_index]
        if right_index < len(level_traverse):
            node.right_child = level_traverse[right_index]

    return level_traverse[0]


def level_display(root):
    """层次遍历

    :param root: BinaryTreeNode
        树的根结点
    :return: List[BinaryTreeNode]
        层次遍历序列
    """
    displays = list()
    #  根结点为空
    if not root:
        return displays

    queue = list()
    queue.append(root)
    while len(queue) != 0:
        current_node = queue.pop(0)
        if not current_node:
            displays.append(current_node)
            continue

        displays.append(current_node.val)
        queue.append(current_node.left_child)
        queue.append(current_node.right_child)

    return displays
