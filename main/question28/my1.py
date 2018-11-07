"""

@Time    : 上午11:21
@Author  : qcymkxyc
@Email   : qcymkxyc@163.com
@File    : my1.py
@Software: PyCharm

通过复制一棵镜像树，再用前序遍历比较复制后的树和原树是否相同

"""
from main.question26 import my1


def reverse_copy_tree(root):
    """复制该树的镜像树

    :param root:BinaryTreeNode
        树的根结点
    :return: BinaryTreeNode
        复制树的根节点
    """
    if not root:
        return

    copy_root = my1.BinaryTreeNode(root.val)

    copy_root.left_child = reverse_copy_tree(root.right_child)
    copy_root.right_child = reverse_copy_tree(root.left_child)

    return copy_root


def pre_is_reverse_same(origin_tree, reverse_tree):
    """用前序遍历检测镜像树和原树是否相同

    :param origin_tree: BinaryTreeNode
        原树节点
    :param reverse_tree: BinaryTreeNode
        镜像反转节点
    :return: bool
        是否相同
    """
    # 当两个节点有一个为空另一个不为空时
    if (origin_tree is None) ^ (reverse_tree is None):
        return False
    # 当两个节点均为空时
    if not (origin_tree and reverse_tree):
        return True

    # 以下是两者均不为空的情况
    # 根结点不同
    if origin_tree.val != reverse_tree.val:
        return False

    # 递归左右子树
    is_same = pre_is_reverse_same(
        origin_tree.left_child, reverse_tree.left_child)
    if is_same:
        pre_is_reverse_same(
            origin_tree.right_child, reverse_tree.right_child)
    return is_same
