#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
 @author:qcymkxyc
 @email:qcymkxyc@163.com
 @software: PyCharm
 @file: my1.py
 @time: 2019/2/1 11:04

"""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def create_link_list(seq):
    """创建链表

    :param seq: List[int]
        序列
    :return: ListNode\
        链表头结点
    """
    head = None
    last_node = None
    for i, val in enumerate(seq):
        c_node = ListNode(val)
        if not head:
            head = c_node
            last_node = c_node
        else:
            last_node.next = c_node
            last_node = c_node

    return head


def display_linklist(head):
    """遍历链表

    :param head: ListNode
        链表头结点
    :return: List[int]
        遍历序列
    """
    c_node = head
    seq = list()
    while c_node:
        seq.append(c_node.val)
        c_node = c_node.next

    return seq


def public_node(link_list1, linklist2):
    """两个链表的公共节点

    :param link_list1: List[int]
        链表1
    :param linklist2: List{int]
        链表2
    :return:int
        节点值
    """
    link_seq1 = list()
    c_node1 = link_list1
    while c_node1:
        link_seq1.append(c_node1)
        c_node1 = c_node1.next

    c_node2 = linklist2
    while c_node2:
        if c_node2 in link_seq1:
            return c_node2
        c_node2 = c_node2.next
