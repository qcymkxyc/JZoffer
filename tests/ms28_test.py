import unittest

from main.question28 import my1, book1
from main.question26 import my1 as q26


class MSTestCase(unittest.TestCase):

    def setUp(self):
        pre_order = ["A", "B", "C", "D", "E", "F"]
        in_order = ["C", "B", "D", "A", "E", "F"]

        self.tree = q26.create_binary_tree(pre_order, in_order)

    def test_my1_pre_is_reverse_same(self):
        # 不对称的情况
        reverse_tree = my1.reverse_copy_tree(self.tree)
        self.assertFalse(my1.pre_is_reverse_same(self.tree, reverse_tree))

        # 对称的情况
        pre_order = [8, 6, 5, 7, 6, 7, 5]
        in_order = [5, 6, 7, 8, 7, 6, 5]
        tree = q26.create_binary_tree(pre_order, in_order)
        reverse_tree = my1.reverse_copy_tree(tree)
        self.assertTrue(my1.pre_is_reverse_same(tree, reverse_tree))

        # 两者均为None
        self.assertTrue(my1.pre_is_reverse_same(None, None))

        # 其中一个为None
        self.assertFalse(my1.pre_is_reverse_same(None, reverse_tree))

    def test_book1_pre_reverse_displayer(self):
        # 不对称的情况
        pre_order_tree = book1.pre_order_displayer(self.tree)
        pre_reverse_tree = book1.pre_reverse_display(self.tree)
        self.assertNotEqual(pre_order_tree, pre_reverse_tree)

        # 对称的情况
        pre_order = [8, 6, 5, 7, 6, 7, 5]
        in_order = [5, 6, 7, 8, 7, 6, 5]
        tree = q26.create_binary_tree(pre_order, in_order)

        pre_order_tree = book1.pre_order_displayer(tree)
        pre_reverse_tree = book1.pre_reverse_display(tree)
        self.assertEqual(pre_order_tree, pre_reverse_tree)

        # None
        self.assertTrue(book1.is_symmetry(None))


if __name__ == '__main__':
    unittest.main()
