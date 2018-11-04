#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 18-11-4 上午11:40
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : my2.py
@Software: PyCharm

扩展:用非递归实现

"""


def reverse_tree(root):
    """反转树

    利用非递归交换左右子树,同非递归的遍历树结构，前序
    中序后序均可，只要能够保证每个节点都能遍历并做交换即可


    :param root: BinaryTreeNode
        树的根节点
    """
    stack = list()

    current_node = root
    while current_node or len(stack):
        if current_node:
            current_node.left_child, current_node.right_child = \
                current_node.right_child, current_node.left_child
            stack.append(current_node)
            current_node = current_node.left_child
        else:
            current_node = stack.pop(0).right_child
