#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 18-10-21 上午11:39
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : my2.py
@Software: PyCharm

题目二
    
"""
from main.question18 import my1


def delete_duplication(head):
    """在一个有序的链表中删除重复结点

    :param head: ListNode
        头结点
    :raises:
        TypeError : 类型不匹配
    """
    if not isinstance(head, my1.ListNode):
        raise TypeError('类型不匹配')

    current_node = head
    next_node = current_node.next
    while current_node and next_node:
        if current_node.value == next_node.value:
            current_node.next = next_node.next
            del next_node
        current_node = current_node.next
        next_node = current_node.next
