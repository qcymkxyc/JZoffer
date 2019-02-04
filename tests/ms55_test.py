import unittest
from main.question55 import book1, book2
from main.question26 import my1 as q26


class MSTestCase(unittest.TestCase):
    def setUp(self):
        pre_order = [1, 2, 4, 5, 7, 3, 6]
        in_order = [4, 2, 7, 5, 1, 3, 6]
        self.root = q26.create_binary_tree(pre_order, in_order)

    def test_book1_tree_depth(self):
        depth = book1.tree_depth(self.root)
        self.assertEqual(4, depth)
        self.assertEqual(0, book1.tree_depth(None))

    def test_book2_is_balance_tree(self):
        self.assertTrue(book2.is_balance_tree(self.root))

        pre_order = [1, 2, 4, 5]
        in_order = [4, 2, 5, 1]
        root = q26.create_binary_tree(pre_order, in_order)
        self.assertFalse(book2.is_balance_tree(root))


if __name__ == '__main__':
    unittest.main()
