# coding=utf-8
"""

@Time    : 下午12:30
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : book1.py
@Software: PyCharm

"""


def pre_reverse_display(root):
    """对称的前序遍历

    :param root: 根结点
        BinaryTreeNode
    :return: list
        前序遍历结果
    """
    if not root:
        return [None]

    displays = list()
    displays.append(root.val)

    displays.extend(pre_reverse_display(root.right_child))
    displays.extend(pre_reverse_display(root.left_child))

    return displays


def pre_order_displayer(root):
    """前序遍历

    :param root: BinaryTreeNode
        树的根结点
    :return: list
        遍历结果
    """
    if not root:
        return [None]

    displays = list()
    displays.append(root.val)

    displays.extend(pre_order_displayer(root.left_child))
    displays.extend(pre_order_displayer(root.right_child))

    return displays


def is_symmetry(root):
    """判度树是否对称

    :param root: BinaryTreeNode
        树的根结点
    :return: bool
        是否对称
    """
    return pre_order_displayer(root) == pre_reverse_display(root)
