#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 上午11:11
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : my3.py
@Software: PyCharm

题目二

"""


def level_display(root):
    """层次遍历二叉树（分行打印）

    该方法的打印用一个多层list存储，即可完成多
    层打印

    :param root: BinaryTreeNode
        树的根结点
    :return: list(list())
        多层打印的list
    """
    displays = list()
    # 如果根结点为空
    if not root:
        return displays

    queue = list()
    queue.append((None, root))

    while len(queue) != 0:
        parent_node, current_node = queue.pop(0)
        # 如果该节点是空节点
        if not current_node:
            continue

        # 添加子节点进队列
        queue.append((current_node, current_node.left_child))
        queue.append((current_node, current_node.right_child))

        # 如果该结点是根结点
        if not parent_node:
            displays.append([current_node])
            continue

        # 添加当前节点
        # 查询父节点的位置
        i = 0
        for i, sub_d in enumerate(displays):
            if parent_node in sub_d:
                break
        if len(displays) == i + 1:
            displays.append(list())
        displays[i + 1].append(current_node)

    for i, v in enumerate(displays):
        displays[i] = [node.val for node in v]

    return displays
