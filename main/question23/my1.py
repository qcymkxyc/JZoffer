#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 18-10-28 上午11:04
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : my1.py
@Software: PyCharm
    
"""


class Node:
    def __init__(self, value=None):
        self.val = value
        self.next = None


def create_linklist(data):
    """创建链表

    :param data: list or tuple
        数据
    :return: Node
        链表的头节点
    """
    head = None
    current_node = head
    for i, val in enumerate(data):
        # 第一个节点处理
        if not current_node:
            current_node = Node(val)
            head = current_node
            continue
        temp_node = Node(val)
        current_node.next = temp_node
        current_node = temp_node

    return head


def display_linklist(head):
    """遍历链表

    :param head: Node
        链表头节点
    :return: list
        遍历结果
    """
    displays = list()
    current_node = head
    while current_node:
        displays.append(current_node.val)
        current_node = current_node.next

    return displays


def first_node_ring(head):
    """找到环中的第一个节点

    :param head: Node
        链表的头节点
    :return: Node or None
        第一个节点或者不存在环返回None
    """
    nodes = list()
    current_node = head
    while current_node:
        # 已存在则表示存在还
        if current_node in nodes:
            return current_node
        nodes.append(current_node)
        current_node = current_node.next

    # 不存在还的情况
    return
