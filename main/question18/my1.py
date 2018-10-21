#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 18-10-21 上午10:39
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : my1.py
@Software: PyCharm

题目1（无法用O（1），仅有O（n））
    
"""


class ListNode:
    """结点"""

    def __init__(self):
        self.value = None
        self.next = None


def delete_node(head, node):
    """删除链表中的node结点

    无法用O(1)实现，仅能用O(n)实现

    :param head: ListNode
        头指针
    :param node: ListNode
        要删除
    :raises:
        TypeError: head或node的类型错误
        ValueError: 未找到node结点
    """
    if not (isinstance(head, ListNode) and isinstance(node, ListNode)):
        raise TypeError("类型不匹配")

    # 删除的结点是head的情况
    if head == node:
        head = head.next
        del head
        return

    # 删除的结点不是head的情况
    current_node = head
    while current_node and current_node.next != node:
        current_node = current_node.next

    # 如果未找到
    if not current_node:
        raise ValueError("未找到node结点")

    # 找到的情况
    current_node.next = node.next
    del node


def create_list(data):
    """根据数据创建链表

    :param data: list or tuple
        数据
    :return: ListNode
        链表的头结点
    """
    head = None
    current_node = head

    for i, value in enumerate(data):
        temp_node = ListNode()
        temp_node.value = value

        if i == 0:
            current_node = temp_node
            head = current_node
        else:
            current_node.next = temp_node
            current_node = temp_node

    return head
