#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 18-10-29 上午11:10
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : my1.py
@Software: PyCharm

"""
from main.question23 import my1


def reverse_linklist(head):
    """反转链表

    :param head: Node
        链表的头节点
    :return: Node
        反转后的头节点
    """
    # 将链表中的元素压入栈中
    current_node = head
    stack = list()
    while current_node:
        stack.append(current_node.val)

        temp = current_node
        current_node = current_node.next
        del temp

    # 出栈并重新建立链表
    # data = stack.reverse()
    data = [stack[i] for i in range(len(stack) - 1, -1, -1)]
    reverse_head = my1.create_linklist(data)

    return reverse_head
