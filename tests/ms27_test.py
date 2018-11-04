import unittest

from main.question27 import my1, my2
from main.question26 import my1 as q26


class MSTestCase(unittest.TestCase):

    def setUp(self):
        # 原树的前序和中序遍历
        self.pre_order = [8, 6, 5, 7, 10, 9, 11]
        self.in_order = [5, 6, 7, 8, 9, 10, 11]

        # 反转后的前序和中序遍历
        self.reverse_pre_order = [8, 10, 11, 9, 6, 7, 5]
        self.reverse_in_order = [11, 10, 9, 8, 7, 6, 5]

    def test_my1_reverse_tree(self):
        # 一般情况
        root = q26.create_binary_tree(self.pre_order, self.in_order)
        my1.reverse_tree(root)
        self.assertEqual(self.reverse_pre_order, q26.pre_order_tree(root))
        self.assertEqual(self.reverse_in_order, q26.in_order_tree(root))

        # 根节点为空的情况
        root = None
        my1.reverse_tree(root)
        self.assertEqual([], q26.pre_order_tree(root))
        self.assertEqual([], q26.in_order_tree(root))

        # 仅有左子树
        pre_order_seq = [1, 2, 3, 4, 5]
        in_order_seq = [5, 4, 3, 2, 1]

        reverse_pre_order_seq = [1, 2, 3, 4, 5]
        reverse_in_order_seq = [1, 2, 3, 4, 5]
        root = q26.create_binary_tree(pre_order_seq, in_order_seq)
        my1.reverse_tree(root)
        self.assertEqual(reverse_pre_order_seq, q26.pre_order_tree(root))
        self.assertEqual(reverse_in_order_seq, q26.in_order_tree(root))

        # 仅有右子树
        pre_order_seq = [1, 2, 3, 4, 5]
        in_order_seq = [1, 2, 3, 4, 5]

        reverse_pre_order_seq = [1, 2, 3, 4, 5]
        reverse_in_order_seq = [5, 4, 3, 2, 1]
        root = q26.create_binary_tree(pre_order_seq, in_order_seq)
        my1.reverse_tree(root)
        self.assertEqual(reverse_pre_order_seq, q26.pre_order_tree(root))
        self.assertEqual(reverse_in_order_seq, q26.in_order_tree(root))

    def test_my2_reverse_tree(self):
        # 一般情况
        root = q26.create_binary_tree(self.pre_order, self.in_order)
        my2.reverse_tree(root)
        self.assertEqual(self.reverse_pre_order, q26.pre_order_tree(root))
        self.assertEqual(self.reverse_in_order, q26.in_order_tree(root))

        # 根节点为空的情况
        root = None
        my1.reverse_tree(root)
        self.assertEqual([], q26.pre_order_tree(root))
        self.assertEqual([], q26.in_order_tree(root))

        # 仅有左子树
        pre_order_seq = [1, 2, 3, 4, 5]
        in_order_seq = [5, 4, 3, 2, 1]

        reverse_pre_order_seq = [1, 2, 3, 4, 5]
        reverse_in_order_seq = [1, 2, 3, 4, 5]
        root = q26.create_binary_tree(pre_order_seq, in_order_seq)
        my1.reverse_tree(root)
        self.assertEqual(reverse_pre_order_seq, q26.pre_order_tree(root))
        self.assertEqual(reverse_in_order_seq, q26.in_order_tree(root))

        # 仅有右子树
        pre_order_seq = [1, 2, 3, 4, 5]
        in_order_seq = [1, 2, 3, 4, 5]

        reverse_pre_order_seq = [1, 2, 3, 4, 5]
        reverse_in_order_seq = [5, 4, 3, 2, 1]
        root = q26.create_binary_tree(pre_order_seq, in_order_seq)
        my1.reverse_tree(root)
        self.assertEqual(reverse_pre_order_seq, q26.pre_order_tree(root))
        self.assertEqual(reverse_in_order_seq, q26.in_order_tree(root))


if __name__ == '__main__':
    unittest.main()
