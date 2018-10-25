#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 18-10-25 上午11:37
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : book1.py
@Software: PyCharm
    
"""
from main.question22 import my1


@my1.check
def find_k_to_tail(head, k):
    """找到末尾的第k个节点

    :param head: Node
        头节点
    :param k: int
        倒数第k个节点
    :return: object
        倒数第k个节点的元素
    :raises:
        TypeError: head为空
        IndexError:
                倒数的index数大于链表长度
                last_index小于0
    """
    first_node, second_node = head, head

    # 循环第一个节点
    for i in range(k):
        try:
            first_node = first_node.next
        except AttributeError:
            raise IndexError("倒数的index数大于链表长度")

    while first_node:
        second_node = second_node.next
        first_node = first_node.next

    return second_node.value
