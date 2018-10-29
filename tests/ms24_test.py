import unittest

from main.question23 import my1 as q23
from main.question24 import my1, book1


class MSTestCase(unittest.TestCase):

    def setUp(self):
        self.data = list(range(10))
        self.head = q23.create_linklist(self.data)

    def test_my1_reverse_linklist(self):
        # 功能测试
        reverse_head = my1.reverse_linklist(self.head)
        self.data.reverse()
        self.assertEqual(self.data, q23.display_linklist(reverse_head))

        # head为None
        reverse_head = my1.reverse_linklist(None)
        self.assertEqual(None, reverse_head)

        # 仅有一个Node
        head = q23.create_linklist([1])
        reverse_head = my1.reverse_linklist(head)
        self.assertEqual(reverse_head.val, head.val)

    def test_book1_reverse_linklist(self):
        # 功能测试
        reverse_head = book1.reverse_linklist(self.head)
        self.data.reverse()
        self.assertEqual(self.data, q23.display_linklist(reverse_head))

        # head为None
        reverse_head = book1.reverse_linklist(None)
        self.assertEqual(None, reverse_head)

        # 仅有一个Node
        head = q23.create_linklist([1])
        reverse_head = book1.reverse_linklist(head)
        self.assertEqual(reverse_head.val, head.val)


if __name__ == '__main__':
    unittest.main()
