import unittest
from main.question52 import my1, book1


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.seq1 = [1, 2, 3, 4, 5]
        self.seq2 = [-1, 2, -3]
        self.link_list1 = my1.create_link_list(self.seq1)
        self.link_list2 = my1.create_link_list(self.seq2)

        c_node1 = self.link_list1
        while c_node1.val:
            if c_node1.val == 4:
                break
            c_node1 = c_node1.next

        c_node2 = self.link_list2
        while c_node2.next:
            c_node2 = c_node2.next

        c_node2.next = c_node1

    def test_linklist12(self):
        self.assertEqual(self.seq1, my1.display_linklist(self.link_list1))
        self.assertEqual(self.seq2 +
                         [4, 5], my1.display_linklist(self.link_list2))

    def test_my1_public_node(self):
        public_n = my1.public_node(self.link_list1, self.link_list2)
        self.assertEqual(4, public_n.val)

        seq1 = list(range(5))
        seq2 = list(range(10, 15))
        linklist1 = my1.create_link_list(seq1)
        linklist2 = my1.create_link_list(seq2)
        self.assertIsNone(my1.public_node(linklist1, linklist2))

    def test_book1_public_node1(self):
        public_n = book1.public_node1(self.link_list1, self.link_list2)
        self.assertEqual(4, public_n.val)

        seq1 = list(range(5))
        seq2 = list(range(10, 15))
        linklist1 = my1.create_link_list(seq1)
        linklist2 = my1.create_link_list(seq2)
        self.assertIsNone(book1.public_node1(linklist1, linklist2))

    def test_book1_public_node2(self):
        public_n = book1.public_node2(self.link_list1, self.link_list2)
        self.assertEqual(4, public_n.val)

        seq1 = list(range(5))
        seq2 = list(range(10, 15))
        linklist1 = my1.create_link_list(seq1)
        linklist2 = my1.create_link_list(seq2)
        self.assertIsNone(book1.public_node2(linklist1, linklist2))


if __name__ == '__main__':
    unittest.main()
