#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 上午11:15
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : my1.py
@Software: PyCharm

"""
import copy


def sum_display_path(root, sum_num):
    """输出树的遍历和为sum_num的所有路径

    :param root: BinaryTreeNode
        树的根结点
    :param sum_num: int
        和
    :return: list(list())
        所有可能路径
    """
    path = list()
    _pre_display(root, sum_num, path)
    return path


def _pre_display(root, sum_num, paths, pre_display=list()):
    """前序遍历树

    该方法是利用前序遍历验证所走的路径的和是否等于sum_num，
    如果相同，则将路径加入paths中。

    :param root: BinaryTreeNode
        树的根结点
    :param sum_num: int
        和
    :param paths: list(list)
        符合规定的路径
    :param pre_display: list
        之前所走的路径
    """
    if not root:
        return

    pre_display.append(root.val)
    if sum(pre_display) == sum_num:
        paths.append(pre_display)

    # 迭代左子树
    left_display = copy.copy(pre_display)
    _pre_display(root.left_child, sum_num, paths, left_display)
    # 迭代右子树
    right_display = copy.copy(pre_display)
    _pre_display(root.right_child, sum_num, paths, right_display)
