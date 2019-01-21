#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 18-11-2 上午10:23
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : my1.py
@Software: PyCharm
    
"""


def merge_linklist(linklist1, linklist2):
    """合并链表，使合并后的链表何必有序

    :param linklist1: Node
        link1的头节点
    :param linklist2: Node
        link2的头节点
    :return: Node
        合并后的头节点
    """
    current_node1 = linklist1
    current_node2 = linklist2

    # link1和link2为空的情况
    if not current_node1:
        return current_node2
    elif not current_node2:
        return current_node1

    head = None
    current_node = head
    while current_node1 and current_node2:
        temp_node = current_node1 if current_node1.val < current_node2.val else current_node2

        # 判断是否头节点
        if current_node:
            current_node.next = temp_node
            current_node = temp_node
        else:
            current_node = temp_node
            head = current_node

        # 两个原节点的指针向前移
        if temp_node == current_node1:
            current_node1 = current_node1.next
        else:
            current_node2 = current_node2.next

    # 添加未遍历的节点
    if current_node1:
        current_node.next = current_node1
    if current_node2:
        current_node.next = current_node2

    return head
