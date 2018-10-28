#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 18-10-28 上午11:38
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : book1.py
@Software: PyCharm
    
"""


def is_ring(head):
    """判断链表中是否有环

    :param head: Node
        链表的头节点
    :return: Node or None
        有环则返回环中的一个节点,否则返回None
    """
    first_node, second_node = head, head
    while first_node and second_node:
        first_node = first_node.next
        second_node = second_node.next.next
        if second_node == first_node:
            return first_node

    return None


def ring_count(current_node):
    """统计环中节点的个数

    :param current_node: Node
        当前节点(该结点必须为环中的一个节点)
    :return: int
        节点个数,如果无环返回0
    """
    start_node = current_node
    count = 1
    while current_node:
        current_node = current_node.next
        if current_node == start_node:
            return count
        count += 1

    # 无环的情况
    return 0


def first_ring_node(head):
    """返回第一个环节点

    :param head: Node
        链表的头节点
    :return: Node or None
        第一个环节点或None
    """
    # 头节点为空
    if not head:
        return None
    # 仅有一个节点
    if not head.next:
        return None

    # 获取环中的一个节点
    ring_node = is_ring(head)
    # 无环的情况
    if not ring_node:
        return None

    # 有环的情况
    count = ring_count(ring_node)
    first_node, second_node = head, head
    for i in range(count):
        second_node = second_node.next

    while True:
        if first_node == second_node:
            return first_node
        first_node = first_node.next
        second_node = second_node.next

    return
