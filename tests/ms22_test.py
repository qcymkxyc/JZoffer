import unittest

from main.question22 import my1, book1, my2


class MSTestCase(unittest.TestCase):

    def setUp(self):
        self.nums = list(range(10))

    def test_my1_create_linklist(self):
        head = my1.create_linklist(nums=self.nums)
        self.assertEqual(self.nums, my1.display_linklist(head))

    def test_my1_last_index_from_linklist(self):
        head = my1.create_linklist(self.nums)
        self.assertEqual(8, my1.last_index_from_linklist(head, 2))

        # 头节点为空的情况
        with self.assertRaises(TypeError):
            my1.last_index_from_linklist(None, 3)

        # k大于长度的情况
        with self.assertRaises(IndexError):
            my1.last_index_from_linklist(head, 20)

        # 0的情况
        with self.assertRaises(ValueError):
            my1.last_index_from_linklist(head, 0)

    def test_book1_find_k_to_tail(self):
        head = my1.create_linklist(self.nums)
        self.assertEqual(8, book1.find_k_to_tail(head, 2))

        # 头节点为空的情况
        with self.assertRaises(TypeError):
            book1.find_k_to_tail(None, 3)

        # k大于长度的情况
        with self.assertRaises(IndexError):
            book1.find_k_to_tail(head, 20)

        # 0的情况
        with self.assertRaises(ValueError):
            book1.find_k_to_tail(head, 0)

    def test_my2_mid_node(self):
        head = my1.create_linklist(self.nums)
        self.assertTrue(my2.mid_node(head).value in (4, 5))

        head = my1.create_linklist(list(range(1, 6)))
        self.assertEqual(3, my2.mid_node(head).value)


if __name__ == '__main__':
    unittest.main()
