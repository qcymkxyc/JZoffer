import unittest
from main.question54 import book1
from main.question26 import my1 as q26


class MSTestCase(unittest.TestCase):
    def setUp(self):
        pre_order = [5, 3, 2, 4, 7, 6, 8]
        in_order = [2, 3, 4, 5, 6, 7, 8]
        self.root = q26.create_binary_tree(pre_order, in_order)

    def test_book1_k_num(self):
        self.assertEqual(4, book1.k_num(self.root, 3))

        with self.assertRaises(IndexError):
            book1.k_num(None, 1)

        with self.assertRaises(ValueError):
            book1.k_num(self.root, 0)


if __name__ == '__main__':
    unittest.main()
