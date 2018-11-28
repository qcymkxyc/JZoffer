#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 下午12:00
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : book1.py
@Software: PyCharm

"""
import copy


def is_bst_post_seq(post_seq):
    """判断序列是否为一个二叉搜索树的后序遍历

    :param post_seq: list
        后序遍历
    :return: bool
        是否是
    """
    temp_seq = copy.copy(post_seq)
    # 为空返回True
    if len(temp_seq) == 0:
        return True

    # 分出左右子树以及根结点
    root = temp_seq.pop(-1)
    i = 0
    while i < len(temp_seq):
        num = temp_seq[i]
        if num > root:
            break
        i += 1

    left_childs = temp_seq[:i]
    right_childs = temp_seq[i:]

    # 检测子树节点是否错误
    for num in right_childs:
        if num < root:
            return False

    # 子树迭代
    flag = is_bst_post_seq(left_childs)
    if flag:
        return is_bst_post_seq(right_childs)
    else:
        return False
