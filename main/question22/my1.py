#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 18-10-25 上午10:50
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : my1.py
@Software: PyCharm
    
"""
from functools import wraps


def check_nums_type(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        nums = args[0] if len(args) != 0 else kwargs["nums"]
        if not isinstance(nums, (list, tuple)):
            raise TypeError("nums类型错误")
        return func(*args, **kwargs)
    return wrapper


def check(func):
    @wraps(func)
    def wrapper(head, last_index):
        if not head:
            raise TypeError("头节点不能为空")
        if last_index <= 0:
            raise ValueError("last_index必须大于0")
        return func(head, last_index)
    return wrapper


class Node:
    """链表结点"""
    def __init__(self, value=None):
        self.value = value
        self.next = None


@check_nums_type
def create_linklist(nums):
    """创建链表

    :param nums: list or tuple
        链表的值
    :return: Node
        链表的头结点
    """
    head = None
    current_node = head
    for num in nums:
        # 头节点的情况
        if not current_node:
            current_node = Node(num)
            head = current_node
            continue
        temp = Node(num)
        current_node.next = temp
        current_node = current_node.next

    return head


def display_linklist(head):
    """遍历链表

    :param head: Node
        链表头节点
    :return: list
        遍历结果
    """
    results = list()

    current_node = head
    while current_node:
        results.append(current_node.value)
        current_node = current_node.next

    return results


@check
def last_index_from_linklist(head, last_index):
    """链表倒数第last_index个结点

    本题用栈实现，用空间换时间

    :param head: Node
        链表的头节点
    :param last_index: int
        倒数的index
    :return: object
        倒数第last_index的元素值
    :raises:
        TypeError: head为空
        IndexError:
                倒数的index数大于链表长度
                last_index小于0
    """
    stack = list()

    # 入栈
    current_node = head
    while current_node:
        stack.append(current_node.value)
        current_node = current_node.next

    # 出栈
    i = 0
    while True:
        try:
            v = stack.pop(-1)
        except IndexError:
            raise IndexError("倒数的index数大于链表长度")

        if i == last_index - 1:
            return v
        i += 1
