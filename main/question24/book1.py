#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 18-10-29 上午11:33
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : book1.py
@Software: PyCharm
    
"""


def reverse_linklist(head):
    """反转链表

    :param head: Node
        链表的头节点
    :return: Node
        反转后的头节点
    """
    # head为空
    if not head:
        return
    # 仅有一个节点的情况
    if not head.next:
        return head

    i_node, j_node = head, head.next
    i_node.next = None
    temp_node = j_node.next
    while temp_node:
        j_node.next = i_node
        i_node = j_node
        j_node = temp_node
        temp_node = j_node.next

    j_node.next = i_node
    reverse_head = j_node
    return reverse_head
