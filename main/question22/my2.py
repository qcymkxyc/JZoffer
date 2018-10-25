#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 18-10-25 下午12:08
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : my2.py
@Software: PyCharm

相关题目

"""


def mid_node(head):
    """找出链表的中间节点

    :param head: Node
        头节点
    :return: Node
        中间节点的元素
    """
    if not head:
        raise ValueError("头节点不能为空")

    first_node, second_node = head, head

    while first_node:
        try:
            first_node = first_node.next
            first_node = first_node.next
            second_node = second_node.next
        except AttributeError:
            return second_node

    return second_node
