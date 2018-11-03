#!/usr/bin/python3
# coding=utf-8
"""

@Time    : 18-11-3 上午10:48
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : my1.py
@Software: PyCharm

"""
import copy


class BinaryTreeNode:
    """二叉树节点"""

    def __init__(self, val):
        self.val = val
        self.left_child = None
        self.right_child = None


def is_sub_tree(tree1, tree2):
    """判断tree2是否是tree1的子树

    分别中序遍历和前序遍历tree1和tree2，如果tree1中的中序和前序
    序列中均包含tree2的序列且顺序相同则表示tree2为tree1的子树（因为
    前序和中序序列已经可以确定一个树了），否则不是

    :param tree1: BinaryTreeNode
        tree1的根节点
    :param tree2: BinaryTreeNode
        tree2的根节点
    :return: bool
        是否为子树
    :raises:
        ValueError : 树为空
    """
    if not (tree1 and tree2):
        raise ValueError("树为空")
    # tree1的前序和中序遍历
    pre_order_tree1 = pre_order_tree(tree1)
    in_order_tree1 = in_order_tree(tree1)

    # tree2的前序和中序遍历
    pre_order_tree2 = pre_order_tree(tree2)
    in_order_tree2 = in_order_tree(tree2)

    if ("".join(pre_order_tree2) in "".join(pre_order_tree1)
            and "".join(in_order_tree2) in "".join(in_order_tree1)):
        return True
    return False


def create_binary_tree(pre_order, in_order):
    """根据前序遍历和中序遍历创建二叉树

    :param pre_order: list or tuple
        前序遍历
    :param in_order: list or tuple
        中序遍历
    :return: BinaryTreeNode
        树的根节点
    :raises:
        ValueError:
            前序遍历和中序遍历长度不匹配
            前序遍历和中序遍历元素不匹配
    """
    pre_order = copy.copy(pre_order)
    in_order = copy.copy(in_order)

    if len(pre_order) != len(in_order):
        raise ValueError("前序遍历和中序遍历长度不匹配")
    if set(pre_order) != set(in_order):
        raise ValueError("前序遍历和中序遍历元素不匹配")

    # 子树没有元素的情况
    if len(pre_order) == 0:
        return

    # 遍历到叶子节点的情况
    if len(pre_order) == 1:
        return BinaryTreeNode(pre_order[0])

    root_elem = pre_order.pop(0)

    # 中序遍历的左右子树
    in_order_left = in_order[: in_order.index(root_elem)]   # 中序遍历左子树
    in_order_right = in_order[in_order.index(root_elem) + 1:]   # 中序遍历右子树

    # 前序遍历的左右子树
    pre_order_left = [elem for elem in pre_order if elem in in_order_left]
    pre_order_right = [elem for elem in pre_order if elem in in_order_right]

    #  建立子树
    root_node = BinaryTreeNode(val=root_elem)
    root_node.left_child = create_binary_tree(pre_order_left, in_order_left)
    root_node.right_child = create_binary_tree(pre_order_right, in_order_right)

    return root_node


def pre_order_tree(tree_root):
    """前序遍历树结构

    :param tree_root: BinaryTreeNode
        树的根节点
    :return: list
        遍历结果
    """
    displays = list()
    if not tree_root:
        return displays

    displays.append(tree_root.val)
    displays.extend(pre_order_tree(tree_root.left_child))
    displays.extend(pre_order_tree(tree_root.right_child))

    return displays


def in_order_tree(tree_root):
    """中序遍历树结构

    :param tree_root: BinaryTreeNode
        树的根节点
    :return: list
        遍历结果
    """
    displays = list()
    if not tree_root:
        return displays

    displays.extend(in_order_tree(tree_root.left_child))
    displays.append(tree_root.val)
    displays.extend(in_order_tree(tree_root.right_child))

    return displays
