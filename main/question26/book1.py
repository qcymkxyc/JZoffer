#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 18-11-3 下午12:06
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : book1.py
@Software: PyCharm

"""


def is_sub_tree(tree1, tree2):
    """判断tree2是否是tree1的子树

    书上是边遍历边检查
    这里同书上一样用前序遍历检测

    :param tree1: BinaryTreeNode
        tree1的根节点
    :param tree2: BinaryTreeNode
        tree2的根节点
    :return: bool
        是否为子树
    :raises:
        ValueError : 树为空
    """
    if not tree2:
        raise ValueError("树为空")
    if not tree1:
        return False

    is_sub = False  # 表示是否已经找到对应子树
    if tree1.val == tree2.val:
        is_sub = pre_order_compare(tree1, tree2)

    # 已经找到则不往左右子树找
    if not is_sub:
        is_sub = is_sub_tree(tree1.left_child, tree2)
    if not is_sub:
        is_sub = is_sub_tree(tree1.right_child, tree2)

    return is_sub


def pre_order_compare(tree1, tree2):
    """前序遍历两棵树是否相同

    :param tree1: BinaryTreeNode
        tree1的根节点
    :param tree2:BinaryTreeNode
        tree2的根节点
    :return: bool
        是否相同
    """
    if not tree2:
        return True

    is_same = False
    if tree1.val == tree2.val:
        is_same = True
    if is_same:
        is_same = pre_order_compare(tree1.left_child, tree2.left_child)
    if is_same:
        is_same = pre_order_compare(tree1.right_child, tree2.right_child)

    return is_same
