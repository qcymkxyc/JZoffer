import unittest
from main.question36 import book1
from main.question26 import my1 as q26


class MSTestCase(unittest.TestCase):

    def setUp(self):
        self.pre_order = [10, 6, 4, 8, 14, 12, 16]
        self.in_order = [4, 6, 8, 10, 12, 14, 16]

        self.root = q26.create_binary_tree(self.pre_order, self.in_order)

    def test_book1_cover_tree2_list(self):
        head = book1.covert_tree_2_list(self.root)
        self.assertEqual(4, head.val)

        # 正序测试
        positive_seq = list()
        current_node = head
        while current_node:
            positive_seq.append(current_node.val)
            current_node = current_node.right_child
        self.assertEqual(positive_seq, self.in_order)

        # 逆序测试
        reverse_seq = list()
        current_node = head
        while current_node.right_child:
            current_node = current_node.right_child
        import copy
        reverse_in_order = copy.copy(self.in_order)
        reverse_in_order.reverse()
        while current_node:
            reverse_seq.append(current_node.val)
            current_node = current_node.left_child
        self.assertEqual(reverse_in_order, reverse_seq)


if __name__ == '__main__':
    unittest.main()
