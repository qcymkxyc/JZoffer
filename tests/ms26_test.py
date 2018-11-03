import unittest

from main.question26 import my1, book1


class MSTestCase(unittest.TestCase):

    def setUp(self):
        self.pre_order = ["A", "B", "C", "D", "E", "F"]
        self.in_order = ["C", "B", "D", "A", "E", "F"]

    def test_my1_create_binary_tree(self):
        pre_order = ["A", "B", "C", "D", "E", "F"]
        in_order = ["C", "B", "D", "A", "E", "F"]

        tree = my1.create_binary_tree(pre_order, in_order)
        self.assertEqual(pre_order, my1.pre_order_tree(tree))
        self.assertEqual(in_order, my1.in_order_tree(tree))

    def test_my1_is_sub_tree(self):
        tree_root = my1.create_binary_tree(self.pre_order, self.in_order)
        # 功能测试
        # 存在子树的情况
        sub_tree = my1.create_binary_tree(["B", "C", "D"], ["C", "B", "D"])
        self.assertTrue(my1.is_sub_tree(tree1=tree_root, tree2=sub_tree))
        # 不存在子树
        sub_tree = my1.create_binary_tree(["B", "E", "D"], ["E", "B", "D"])
        self.assertFalse(my1.is_sub_tree(tree1=tree_root, tree2=sub_tree))

        # 母树为空
        with self.assertRaises(ValueError):
            my1.is_sub_tree(None, sub_tree)

        # 子树为为空
        with self.assertRaises(ValueError):
            my1.is_sub_tree(tree_root, None)

    def test_book1_is_sub_tree(self):
        tree_root = my1.create_binary_tree(self.pre_order, self.in_order)
        # 功能测试
        # 存在子树的情况
        sub_tree = my1.create_binary_tree(["B", "C", "D"], ["C", "B", "D"])
        self.assertTrue(book1.is_sub_tree(tree1=tree_root, tree2=sub_tree))

        # 不存在子树
        sub_tree = my1.create_binary_tree(["B", "E", "D"], ["E", "B", "D"])
        self.assertFalse(book1.is_sub_tree(tree1=tree_root, tree2=sub_tree))

        # 母树为空
        self.assertFalse(book1.is_sub_tree(None, sub_tree))

        # 子树为为空
        with self.assertRaises(ValueError):
            my1.is_sub_tree(tree_root, None)


if __name__ == '__main__':
    unittest.main()
