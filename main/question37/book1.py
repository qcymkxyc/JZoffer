#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
    @Time :    18-12-14 下午12:51
    @Author:  qcymkxyc
    @File: book1.py
    @Software: PyCharm


"""
import pickle
from main.question26 import my1 as q26


def serialize(root):
    """前序遍历序列化

    :param root: BinaryTreeNode
         树的根结点
    :return: bytes

    """
    pre_traverse = pre_order(root)
    return pickle.dumps(pre_traverse)


def deserialize(pre_traverse_bytes):
    """反序列化

    :param pre_traverse_bytes: bytes
       序列化的二进制
    :return: BinaryTreeNode
        树的根结点
    """
    pre_traverse = pickle.loads(pre_traverse_bytes)


def un_pre_order(pre_order_seq, i=0):
    """

    :param pre_order_seq:
    :return:
    """
    val = pre_order_seq[i]
    if not val:
        return
    node = q26.BinaryTreeNode(val)
    # TODO


def pre_order(root):
    """前序遍历

    :param root:BinaryTreeNode
        树的根结点
    :return:List[int]
        遍历结果（包括None）
    """
    displays = list()
    if not root:
        displays.append(None)
        return displays

    displays.append(root.val)
    displays.extend(pre_order(root.left_child))
    displays.extend(pre_order(root.right_child))

    return displays
