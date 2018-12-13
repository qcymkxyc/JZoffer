#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
    @Time :    18-12-13 下午12:11
    @Author:  qcymkxyc
    @File: book1.py
    @Software: PyCharm


"""
last_node = None


def covert_tree_2_list(root):
    if not root:
        return root

    search_tree_2_list(root)
    head = root

    # 找头节点
    while head.left_child:
        head = head.left_child

    return head


def search_tree_2_list(root):
    """

    :param root:
    :return:
    """
    if not root:
        return

    global last_node
    search_tree_2_list(root.left_child)

    root.left_child = last_node
    if last_node:
        last_node.right_child = root

    last_node = root

    search_tree_2_list(root.right_child)
