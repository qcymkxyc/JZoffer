#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
    @Time :    19-1-29 上午11:10
    @Author:  qcymkxyc
    @File: my1.py
    @Software: PyCharm


"""


class LinkNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkList:
    @staticmethod
    def create_link(seq):
        """

        :param seq:
        :return:
        """
        head = None
        last_node = None
        for i, num in enumerate(seq):
            c_node = LinkNode(num)
            if not head:
                head = c_node
                last_node = c_node
            else:
                last_node.next = c_node
                last_node = c_node

        return head


def reverse_display(head):
    """逆序打印链表

    :param head: LinkNode
        链表头节点
    :return:
    """
    stack = list()
    c_node = head
    while c_node:
        stack.append(c_node.val)
        c_node = c_node.next

    displays = list()
    while len(stack) > 0:
        displays.append(stack.pop(-1))

    return displays
