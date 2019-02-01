#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
 @author:qcymkxyc
 @email:qcymkxyc@163.com
 @software: PyCharm
 @file: book1.py
 @time: 2019/2/1 11:43

"""


def public_node1(link_list1, linklist2):
    """两个链表的公共节点

    :param link_list1: List[int]
        链表1
    :param linklist2: List{int]
        链表2
    :return:int
        节点值
    """
    stack1 = list()
    stack2 = list()
    c_node1 = link_list1
    c_node2 = linklist2

    while c_node1:
        stack1.append(c_node1)
        c_node1 = c_node1.next

    while c_node2:
        stack2.append(c_node2)
        c_node2 = c_node2.next

    # 出栈对比
    first_public_node = None
    while len(stack1) != 0 and len(stack2) != 0:
        node1 = stack1.pop(-1)
        node2 = stack2.pop(-1)

        if node1 == node2:
            first_public_node = node1

    return first_public_node


def public_node2(link_list1, linklist2):
    """两个链表的公共节点

    :param link_list1: List[int]
        链表1
    :param linklist2: List{int]
        链表2
    :return:int
        节点值
    """
    # 计算节点的个数
    c_node1 = link_list1
    c_count1 = 0
    while c_node1:
        c_count1 += 1
        c_node1 = c_node1.next

    c_node2 = linklist2
    c_count2 = 0
    while c_node2:
        c_count2 += 1
        c_node2 = c_node2.next

    # 节点个数对齐
    dis = c_count1 - c_count2
    c_node1, c_node2 = link_list1, linklist2
    if dis >= 0:
        for i in range(dis):
            c_node1 = c_node1.next
    else:
        for i in range(-dis):
            c_node2 = c_node2.next

    # 查找公共节点
    while c_node1 and c_node2:
        if c_node1 == c_node2:
            return c_node1

        c_node1 = c_node1.next
        c_node2 = c_node2.next
